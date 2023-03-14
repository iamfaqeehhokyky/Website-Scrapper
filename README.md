# Website-Scrapper

This Python program scrapes data from a website using the Beautiful Soup library. It includes methods to extract links and images from the website page, and saves the data to text files. See samples in the `X_scrapped_data` folder.

## Installation

- Download the repository or clone it using `git clone https://github.com/iamfaqeehhokyky/Website-Scrapper.git`
- Install the requirements by running `pip install -r requirements.txt`

## Usage after completing the task

1. Replace the url variable in the example usage with the URL of the website you want to scrape
2. Run the program by running `python web_scrapper.py`
3. The program will automatically create a folder in the same directory called `scrapped_data` and all the scraped data will be saved to text files in that folder as (`{url}.txt` and `{url}_img.txt`)

## Explaining the code

This code defines a `WebScraper` class with two methods: `scrape_links` and `scrape_images`. The constructor takes a `url` parameter and initializes an instance variable with it. Since we also imprted the `urlparse` function from the `urllib.parse` module, we are also using it to extract the domain name from the URL. We then use the domain name to construct the file names for the links and images files. For example, if you run the scraper on the URL https://example.com, the links will be saved in `scrapped_data/example.com.txt` and the images will be saved in `scrapped_data/example.com_img.txt`. This way, each domain will have its own separate file for links and images.

The `scrape_links` method sends an HTTP GET request to the URL, parses the HTML content with Beautiful Soup, finds all links on the page, and returns a list of tuples containing the URLs and text of each link. The `scrape_images` method does the same thing but finds all image tags on the page and returns a list of the image URLs.

## Examples

After running the [COMPLETED] program to scrape data from the Kibo website, https://www.kibo.school, here are some examples of the data that the program can scrape:

`www.kibo.school.txt`

```txt
URL: https://kibo.school/degree/admissions/
Text: Applications are open for the July cohort of the online BSc in computer science. Learn more and apply!
URL: /
Text:
URL: #
Text:
URL: None
Text: Degree Program ▾
URL: https://kibo.school/degree/
Text: Overview
URL: https://kibo.school/degree/admissions/
Text: Admissions
URL: https://kibo.school/degree/tuition-aid/
Text: Tuition & Aid
URL: https://kibo.school/degree/curriculum/
Text: Curriculum
URL: https://kibo.school/degree/career/
...
```

`www.kibo.school_img.txt`

```txt
https://www.facebook.com/tr?id=417229956740074&ev=PageView&noscript=1
https://kibo.school/wp-content/uploads/2021/09/Kibo-school-secondary-logo.svg
https://kibo.school/wp-content/uploads/2023/03/Kibo-Header-Image.png
https://kibo.school/wp-content/uploads/2022/06/The-Kibo-Experience.jpg
https://kibo.school/wp-content/uploads/2022/05/Build-your-knowledge-1024x619.jpg
https://kibo.school/wp-content/uploads/2022/06/Build-your-tribe-1024x625.jpg
https://kibo.school/wp-content/uploads/2022/05/Build-real-things-1024x617.jpg
https://kibo.school/wp-content/uploads/2022/05/BSc-in-Computer-Science-1-1024x688.jpg
https://kibo.school/wp-content/uploads/2022/05/Try-Kibo-1024x941.jpg
https://kibo.school/wp-content/uploads/2022/05/Humans-Adesola-1024x1024.jpg
...
```

## Tasks

Your tasks will be to first study the code you already have in the repository then complete the `scrape_links` and `scrape_images` modules inside the class:

1. For the `scrape_links` module, write your code to open the `links_file` in write mode, so that you can have all of the scrapped data that has already been saved to a variable called `links`.
2. For the `scrape_images` module, write your code to open the `images_file` in write mode as well, so that you can have all of the scrapped data that has already been saved to a variable called `images`

## Hints

- The `links_file` and the `images_file` parameters have been declared for you inside the constructor.
- You will need to add the `encoding='utf-8'` parameter to the `open` function, otherwise you will run into a traceback error with encoding characters in the output file.
- Remember to use the python new line syntax `\n`, otherwise, all of the scrapped data will be displayed in a single line.

## Further Samples

Please open the `scrapped_data` folder, to see the sample of the complete scrapped data from the Kibo Website https://www.kibo.school.

Once you complete the tasks in this project, your output files should look similar.
