# Kodak Pulse Downloader

Free your photographs from Kodak Pulse's lock-in before their servers shutdown
for good!

## Getting Started

To start, clone this repository to a comfortable working directory.

```
cd path/to/cool/dir
git clone https://github.com/nicholasyager/kodak-pulse-downloader.git
```

Next, download the required python dependencies listed in `requirements.txt`.

```
pip install -r requirements.txt
```

Now, we're ready to start downloading. Be sure to replace [USERNAME] and
[PASSWORD] with your Kodak Pulse username and password.

```
scrapy runspider spiders/KodakPulseSpider.py -a username=[USERNAME] -a password=[PASSWORD]
```

If login was successful, your Kodak pulse images will be downloaded to the
`images/` directory. Relish in a celebratory cup of coffee knowing that your
photos are now in your control once again. ☕

## Configuration

You can configure the destination directory by modifying the `IMAGES_STORE`
configuration value in the `settings.py` file.

```
# Original
IMAGES_STORE = 'images'

# New
IMAGES_STORE = 'totaly/rad/relative/directory'
```
