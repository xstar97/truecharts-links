OUTPUT_DIR = "output/"
BUILD_DIR = "build/"
TEMP_DIR = "temp/"
DOWNLOADS_DIR = "downloads/"
BRANDS_CSS_FILE = "{}/css/brands.css"
REDIRECTS_FILE = "_redirects"
TEMPLATE_HTML = "templates/index.html"
INDEX_NAME = "{}.html"
IMAGES_ICONS = "{}/images/icons/{}.svg"

DOWNLOAD_URL = "https://github.com/sethcottle/littlelink/archive/refs/tags/{}.zip"
DOWNLOAD_TAG_DEF_VER = "v2.3.4"
DOWNLOAD_ZIP_NAME = "{}.zip"

DOWNLOAD_TAG_VER = "DOWNLOAD_TAG_VER"

CONFIG_BASE_SHORT_URL = "BASE_SHORT_URL"

# Meta
CONFIG_META_ICON_URL = "ICON_URL"
CONFIG_META_TITLE = "TITLE"
CONFIG_META_AUTHOR = "AUTHOR"
CONFIG_META_DESCRIPTION = "DESCRIPTION"
CONFIG_META_THEME = "THEME"

# Bio
CONFIG_BIO_ICON_URL = "ICON_URL"
CONFIG_BIO_ICON_TITLE = "TITLE"
CONFIG_BIO_DESCRIPTION = "DESCRIPTION"
CONFIG_BIO_FOOTER = "FOOTER"

# Button Links
CONFIG_LINKS = "LINKS"

CONFIG_LINKS_KEY_BRAND = "brand"
CONFIG_LINKS_KEY_ICON = "icon"
CONFIG_LINKS_KEY_NAME = "name"
CONFIG_LINKS_KEY_LINK = "link"
CONFIG_LINKS_KEY_REDIRECTS = "redirects"

BUTTON_CLASS_NAME = '.button.button-{}'
BUTTON_DETAILS_DEF_BRAND = "web"
BUTTON_DETAILS_DEF_NAME = "Google"
BUTTON_DETAILS_DEF_ICON = "generic-website"
BUTTON_DETAILS_DEF_LINK = "https://google.com"

# _REDIRECTS
ENABLE_REDIRECTS = "ENABLE_REDIRECTS"

CONFIG_REDIRECTS_KEY_SRC = "src"
CONFIG_REDIRECTS_KEY_DEST = "dest"
CONFIG_REDIRECTS_KEY_CODE = "code"

# Define the list of files and directories to delete
FILES_TO_DELETE = [
    'privacy.html',
    'images/littlelink.png',
    'images/littlelink.svg',
    'images/littlelink@2x.png',
    'LICENSE.md',
    'README.md',
    '.git',
    '.github',
    '.gitignore'
]
