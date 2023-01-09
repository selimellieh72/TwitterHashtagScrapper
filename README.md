<h1 align="center">
  TwitterHashtagScrapper
</h1>

<p align="center">
  <a href="#motivation">About</a> •
  <a href="#key-features">Configuration</a> •
  <a href="#how-to-use">How To Use</a> •
  <a href="#credits">Credits</a>

</p>

## About

TwitterHashtagScrapper is a handful Python script that scraps any number of tweets for a given hashtag name. The script is configurable and customizable as needed. I've made it originally for a client but since then I've decided to make it open source.

## Configuration

- account.txt<br/>

  - Start by replacing [username] and [password] with your own username and password for your Twitter account. The script will use this account to login and scrap the posts.

- hashtags.txt<br/>

  - In hashtags.txt, you can write down any number of hashtags you want to scrap posts for. (Seperated by new lines)

## How To Use

> **Warning**
> Before using the script, make sure you've configured it properly and made the necessary adjustments as per the Configuration section.

To clone and run this application, you'll need [Python](https://www.python.org/downloads/) installed on your system. From your command line:

```bash
# Clone this repository
$ git clone https://github.com/selimellieh72/MetaMedApp

# Go into the repository
$ cd TwitterHashtagScrapper

# Install dependencies
$ pip install -r requirements.txt

# Run the app
python main.py [QUERY_LENGTH]
```

> **Disclaimer** 
> [QUERY_LENGTH] here means the minimum number of tweets for each hashtag. If not provided, will default to 50.

## Credits

- [Python](https://python.org)
- [Selenium](https://www.selenium.dev/)

---

> [selimellieh.me](https://www.selimellieh.me) &nbsp;&middot;&nbsp;
> GitHub [@selimellieh72](https://github.com/selimellieh72) &nbsp;&middot;&nbsp;
> Twitter [@selim_ellieh](https://twitter.com/selim_ellieh)
