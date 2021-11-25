import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id="ResultsContainer")

job_elements = results.find_all("div", class_="card-content")

#job_elements = soup.find(id="ResultsContainer").find_all("div", class_="card-content")

#Get Text of Different Jobs
for job_element in job_elements:
    title_element = job_element.find("h2", class_="title")
    print(title_element.text.strip())
    print()

#Sees how many python jobs are available on this site
python_jobs = results.find_all(
    "h2", string=lambda text: "python" in text.lower()
)
print(len(python_jobs))

python_job_elements = [
    h2_element.parent.parent.parent for h2_element in python_jobs
]

#Get Different Links
for job_element in python_job_elements:
    # -- snip --
    links = job_element.find_all("a")
    for link in links:
        link_url = link["href"]
        print(f"Apply here: {link_url}\n")

