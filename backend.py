# imports from config.py
from config_data import *

import os,shutil,json,urllib.request,zipfile,io,urllib.parse,glob,sys

def load_config_by_file(file_name):
    print(f"loading config from file: {file_name}...")
    # Load the configuration JSON file
    with open(f"{file_name}", "r") as f:
        config_json = f.read()
    try:
        config = json.loads(config_json)
        print(json.dumps(config, indent=4))
        return config
    except ValueError:
        print('Invalid configuration object')
        exit(1)

def load_config_by_json(config_json):
    try:
        config = json.loads(config_json)
        print(json.dumps(config, indent=4))
        return config
    except ValueError:
        print('Invalid configuration object')
        exit(1)

def delete_dir(dir_path):
    try:
        # If the directory exists, delete it recursively
        if os.path.exists(dir_path):
            shutil.rmtree(dir_path)
            print(f'Deleted directory: {dir_path}')

        # Create the directory
        os.makedirs(dir_path)
        print(f'Created directory: {dir_path}')
    except Exception as e:
        print(f'Error: {e}')

def extract_zip(downloads_zip_path, temp_dir_path):
    # Extract the contents to the temporary directory
    print('Extracting repository contents...')
    with zipfile.ZipFile(downloads_zip_path, 'r') as zip_ref:
        extracted_dir = zip_ref.namelist()[0]
        extracted_path = os.path.join(temp_dir_path, extracted_dir)
        zip_ref.extractall(temp_dir_path)
    print('Repository contents extracted successfully.')

    # Move all files to the temp directory
    print('Moving all files to the temp directory...')
    for item in os.listdir(extracted_path):
        item_path = os.path.join(extracted_path, item)
        shutil.move(item_path, temp_dir_path)
    print('All files moved successfully.')
    
    return temp_dir_path

def download_zip(temp_dir_path, tag_ver):
    zip_name = DOWNLOAD_ZIP_NAME.format(tag_ver)
    downloads_zip_path = os.path.join(DOWNLOADS_DIR, zip_name)

    # Check if temp directory already contains files
    if os.path.exists(temp_dir_path) and os.listdir(temp_dir_path):
        print('Temp directory already contains files, skipping download and extraction.')
        return temp_dir_path

    # Check if zip file already exists in downloads directory
    if os.path.exists(downloads_zip_path):
        print('Zip file already exists in downloads directory, skipping download.')
    else:
        # Download the zip file
        os.mkdir(DOWNLOADS_DIR)
        print('Downloading repository from {}...'.format(DOWNLOAD_URL.format(tag_ver)))
        response = urllib.request.urlopen(DOWNLOAD_URL.format(tag_ver))
        with open(downloads_zip_path, 'wb') as f:
            f.write(response.read())
        print('Repository downloaded successfully.')

    # Extract the contents to the temporary directory
    extract_zip(downloads_zip_path, temp_dir_path)

    # Move all files to the temp directory
    print('Moving all files to the temp directory...')
    #for item in os.listdir(temp_dir_path):
    #    item_path = os.path.join(temp_dir_path, item)
    #    #shutil.move(item_path, temp_dir_path)
    #print('All files moved successfully.')

    return temp_dir_path

def copy_icon_if_needed(config, temp_dir_path):
    meta_icon_url = config.get("META", {}).get("ICON_URL", "")
    bio_icon_url = config.get("BIO", {}).get("ICON_URL", "")
    print("\ncheck assets dir for icon and favicon files...\n")

    def copy_local_file(source_url, destination_path):
        source_path = os.path.normpath(source_url)
        try:
            # Check if the source file exists
            if os.path.exists(source_path):
                # Copy the file to the destination folder
                shutil.copy(source_path, destination_path)
                print(f"{source_path} copied successfully.")
            else:
                print(f"\nSource file {source_path} not found.")
        except Exception as e:
            print(f"Error copying {source_path}: {str(e)}")

    if meta_icon_url == "favicon.png":
        copy_local_file("./assets/favicon.png", os.path.join(temp_dir_path, "favicon.png"))
    if bio_icon_url == "icon.png":
        copy_local_file("./assets/icon.png", os.path.join(temp_dir_path, "icon.png"))
    else:
        print("\nICON_URL does not match 'favicon.png' or 'icon.png' in either META or BIO, likely using a url for the image.")

def copy_temp_to_build(temp_dir_path, build_dir_path, name_index):
    # Find the directory with index.html
    while not os.path.exists(os.path.join(temp_dir_path, name_index)):
        temp_dir_path = os.path.join(temp_dir_path, os.listdir(temp_dir_path)[0])
        
    # Copy files and directories to build directory
    for item in os.listdir(temp_dir_path):
        item_path = os.path.join(temp_dir_path, item)
        if os.path.isfile(item_path):
            shutil.copy(item_path, build_dir_path)
        elif os.path.isdir(item_path):
            shutil.copytree(item_path, os.path.join(build_dir_path, item))
        else:
            print(f"\nUnsupported file type: {item_path}")

def validate_button_class(dir_path,name):
    path = BRANDS_CSS_FILE.format(dir_path)
    with open(path, 'r') as f:
        css = f.read()

    button_class = BUTTON_CLASS_NAME.format(name)
    
    return button_class in css

def validate_button_image(dir_path,name):
    path = IMAGES_ICONS.format(dir_path,name)
    return os.path.exists(path)

def generate_buttons_html(config,dir_path):
    # Extract the button details from the LINKS object list
    buttons = config[CONFIG_LINKS]
    button_details = [(button.get(CONFIG_LINKS_KEY_BRAND, BUTTON_DETAILS_DEF_BRAND), button.get(CONFIG_LINKS_KEY_NAME, BUTTON_DETAILS_DEF_NAME), button.get(CONFIG_LINKS_KEY_ICON, BUTTON_DETAILS_DEF_ICON), button.get(CONFIG_LINKS_KEY_LINK, BUTTON_DETAILS_DEF_LINK)) for button in buttons]

    # Generate new HTML code for the buttons
    button_html = ''
    for button_brand, button_name, button_icon, button_link in button_details:
        button_link = "{}".format(button_link)
        
        if not config[CONFIG_BASE_SHORT_URL] is None:
            button_link = config[CONFIG_BASE_SHORT_URL] + button_link

        if not validate_button_class(dir_path,button_brand):
            button_brand = BUTTON_DETAILS_DEF_BRAND

        if not validate_button_image(dir_path,button_icon):
            button_icon = BUTTON_DETAILS_DEF_ICON

        print(f"\nbutton: {button_brand}\nurl: {button_link}\nicon: {button_icon}\nname: {button_name}")
        button_html += '\t\t\t\t<!-- %s -->\n' % button_name
        button_html += '\t\t\t\t<a class="button button-%s" href="%s" target="_blank" rel="noopener" role="button"><img class="icon" src="images/icons/%s.svg" alt="">%s</a><br>\n' % (button_brand, button_link, button_icon, button_name)

    return button_html

def generate_index_html(config, dir_path, name_index):
    # Read HTML file
    with open(TEMPLATE_HTML, 'r') as f:
        html = f.read()

    # Replace variables in HTML
    replaced_html = html \
        .replace('{{META_ICON_URL}}', config["META"][CONFIG_META_ICON_URL]) \
        .replace('{{META_TITLE}}', config["META"][CONFIG_META_TITLE]) \
        .replace('{{META_AUTHOR}}', config["META"][CONFIG_META_AUTHOR]) \
        .replace('{{META_DESCRIPTION}}', config["META"][CONFIG_META_DESCRIPTION]) \
        .replace('{{META_THEME}}', config["META"][CONFIG_META_THEME]) \
        .replace('{{BIO_ICON_URL}}', config["BIO"][CONFIG_BIO_ICON_URL]) \
        .replace('{{BIO_TITLE}}', config["BIO"][CONFIG_BIO_ICON_TITLE]) \
        .replace('{{BIO_DESCRIPTION}}', config["BIO"][CONFIG_BIO_DESCRIPTION]) \
        .replace('{{BIO_FOOTER}}', config["BIO"][CONFIG_BIO_FOOTER]) \
        .replace('{{BIO_BUTTONS}}', generate_buttons_html(config,dir_path))

    # Write replaced HTML back to file
    with open(os.path.join(dir_path, name_index), 'w') as f:
        f.write(replaced_html)

    print('\nHTML file updated!')

def delete_unnecessary_files(dir_path):
    print('Deleting unnecessary files and directories...')
    for file_path in FILES_TO_DELETE:
        full_path = os.path.join(dir_path, file_path)
        try:
            if os.path.isdir(full_path):
                if file_path.startswith("littlelink-"):
                    shutil.rmtree(full_path)
                    print('Removed directory: {}'.format(full_path))
            elif os.path.exists(full_path):
                os.remove(full_path)
                print('Removed file: {}'.format(full_path))
        except Exception as e:
            print('Error deleting {}: {}'.format(full_path, e))
    
    # Add code to delete folders starting with "littlelink-"
    for item in os.listdir(dir_path):
        full_path = os.path.join(dir_path, item)
        try:
            if os.path.isdir(full_path) and (item.startswith("littlelink-") or item.startswith(".")):
                shutil.rmtree(full_path)
                print('Removed directory: {}'.format(full_path))
        except Exception as e:
            print('Error deleting {}: {}'.format(full_path, e))
    
    print('Deletion complete!')

def generate_redirects_file(config, dir_path):
    # Check if ENABLE_REDIRECTS is enabled
    enable_redirects = config.get(ENABLE_REDIRECTS, False)

    # Initialize an empty list to store the redirect entries
    redirect_entries = []

    # Check if redirects are enabled before processing
    if enable_redirects:
        # Loop through each object in the "LINKS" array
        for link in config[CONFIG_LINKS]:
            redirects = link.get(CONFIG_LINKS_KEY_REDIRECTS)
            if redirects:
                for redirect in redirects:
                    src = redirect[CONFIG_REDIRECTS_KEY_SRC]
                    dest = redirect[CONFIG_REDIRECTS_KEY_DEST]
                    code = redirect[CONFIG_REDIRECTS_KEY_CODE]
                    redirect_entries.append(f"{src} {dest} {code}")
    # Generate the _redirects file content if redirects are enabled
    if enable_redirects:
        redirects_file_path = os.path.join(dir_path, REDIRECTS_FILE)
        with open(redirects_file_path, 'w') as file:
            file.write("\n".join(redirect_entries))
        print("Generated _redirects file:\n" + "\n".join(redirect_entries))
    else:
        print("Redirects are not enabled, so the _redirects file is not generated.")
