# imports from config.py
from config_data import *
from backend import *
import argparse
import os
from dotenv import load_dotenv

def main(config_file):
    
    # Load configuration
    config = load_config_by_file(config_file)
    
    # Check tag version for download url
    ver_tag = config.get(DOWNLOAD_TAG_VER, DOWNLOAD_TAG_DEF_VER)
    print(f'tag version to download: {ver_tag}')

    # Define paths
    html_index_name = INDEX_NAME.format("index")
    build_dir_path = os.path.join(os.getcwd(), BUILD_DIR.format("index"))
        
    html_path = os.path.join(build_dir_path, html_index_name)
    
    temp_dir_path = os.path.join(os.getcwd(), TEMP_DIR.format("index"))

    print(f'\nbuild_dir_path: {build_dir_path}\nhtml_path: {html_path}\ntemp: {temp_dir_path}')

    # Delete old build directory and create new one
    delete_dir(build_dir_path)
    delete_dir(temp_dir_path)

    # Download LittleLink repository
    _tempDIR = download_zip(temp_dir_path,ver_tag)
    
    # Delete unnecessary files and directories
    delete_unnecessary_files(_tempDIR)

    # Generate HTML file
    generate_index_html(config,_tempDIR,html_index_name)
    
    # Generate a _redirect file
    generate_redirects_file(config,_tempDIR)

    # Add local file if needed
    copy_icon_if_needed(config, temp_dir_path)

    # Copy temp to the build dir.
    copy_temp_to_build(temp_dir_path, build_dir_path, html_index_name)
    print(f"\ncopied {temp_dir_path} to {build_dir_path}")

if __name__ == '__main__': 
    load_dotenv()
    links_json_name = os.getenv('LINKS_JSON_NAME', './assets/links.json')
    main(links_json_name)
