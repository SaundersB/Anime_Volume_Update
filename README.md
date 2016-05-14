# Anime_Volume_Update
This Python script will scrape www.mangapanda.com for any anime you wish to know has a new volume available. I've used it to track both the Dragon Ball Super and One Piece anime. But you can create a Selenium webdriver and Anime object of your own. This script will only text your phone if there is a new version each day. I use crontab to schedule it to run once a day. That way when a new anime is released I know about it as soon as possible and don't have to check the site myself daily.


## Installation
1. `git clone git@github.com:SaundersB/Anime_Volume_Update.git`
2. Edit the phone number, cell phone carrier, gmail username and password. If you want to use another carrier other than AT&T or email provider other than gmail you'll have to change those.
3. Edit the usage of the WebDriver, Text, and Anime classes. If you want to track a different anime just make sure to pass in the correct url, anime name, and tracking file.
4. `crontab -e`
5. Append the line: `00 21 * * * /Users/username/Anime_Volume_Update/Anime_Issue_Update.py` (You can change the frequency however you want).
6. Enjoy!


## Usage

Use this script to track your favorite anime on http://www.mangapanda.com/. Once it checks the newest volumes against the previously saved volumes from a text file it will send you a text message if a new volume is released.

## Contributing

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D

## Credits

self.me = me

## License

MIT License

Copyright (c) [year] [fullname]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
