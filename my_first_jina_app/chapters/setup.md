# 💾 My First Jina App: Setup

## 🗝️ Key Concepts

First of all, read up on [Jina 101](https://github.com/jina-ai/jina/tree/master/docs/chapters/101) so you have a clear understanding of how Jina works. We're going to refer to those concepts a lot. We assume you already have some knowledge of Python and machine learning.

## 🧪 Try it Out!

Before actually downloading, configuring and testing your app, let's get an idea of the finished product:

### Deploy with Docker

We've prepared a Docker image with indexed data. You can run it with:

```bash
docker run -p 45678:45678 jinaai/hub.app.distilbert-southpark
```

Check out more details about the Docker image [here](rest-api/README.md).

Note: You'll need to run the Docker image before trying the steps below

#### Query with Jinabox

![](../jinabox-southpark.gif)

1. Go to [jinabox](https://jina.ai/jinabox.js) in your browser
2. Ensure you have the server endpoint set to `http://localhost:45678/api/search`
3. Type a phrase into the search bar and see which South Park lines come up

Find out more about [jinabox.js](https://github.com/jina-ai/jinabox.js/), including how to use the front-end code in your own project.

#### Query with `curl`

Alternatively, you can open your shell and check the results via the RESTful API. The matched results are stored in `topkResults`.

```bash
curl --request POST -d '{"top_k": 10, "mode": "search", "data": ["text:hey, dude"]}' -H 'Content-Type: application/json' 'http://0.0.0.0:45678/api/search'
```

<details>
  <summary>See console output</summary>

```json  
{
  "search": {
    "docs": [
      {
        "chunks": [
          {
            "chunkId": 225641550,
            "embedding": {},
            "weight": 1.0,
            "length": 1,
            "topkResults": [
              {
                "matchChunk": {
                  "docId": 7,
                  "chunkId": 401451721,
                  "offset": 1,
                  "weight": 1.0,
                  "length": 2,
                  "mimeType": "text/plain",
                  "location": [
                    6,
                    17
                  ]
                },
                "score": {
                  "value": 3.5258932,
                  "opName": "NumpyIndexer"
                }
              }
            ],
            "mimeType": "text/plain",
            "location": [
              0,
              10
            ]
          }
        ],
        "weight": 1.0,
        "length": 1,
        "topkResults": [
          {
            "matchDoc": {
              "docId": 7,
              "weight": 1.0,
              "mimeType": "text/plain",
              "text": "Satan! Good-bye.\n"
            },
            "score": {
              "value": 0.7486778,
              "opName": "BiMatchRanker"
            }
          }
        ],
        "mimeType": "text/plain",
        "text": "text:Hello"
      }
    ],
    "topK": 1
  },
  "status": {}
}
```

</details>

## 🐍 Install

### Prerequisites

You'll need:

* Basic knowledge of Python
* Python 3.7 or higher installed, and pip
* A Mac or Linux computer (we don't currently support Windows)
* 8 gigabytes or more of RAM
* Plenty of time - Indexing can take a while!

You should have also read [key concepts](concepts.md) to get a good overview of how Jina and this example work.

### Clone this repo

Let's get the basic files we need to get moving:

```
git clone XXX/tutorial
cd tutorial
```

### Cookiecutter

```
pip install -U cookiecutter && cookiecutter gh:jina-ai/cookiecutter-jina
```

We use [cookiecutter](https://github.com/cookiecutter/cookiecutter) to spin up a basic Jina app and save you having to do a lot of typing and setup. 

For our South Park example, we recommend the following settings:

* Project name: `South Park`
* Project slug: `south_park`
* Task type: `nlp`
* Index type: `strings`

All other fields you can just fill in however you please.

## 📂 Files and Folders

After running `cookiecutter`, you should see a bunch of files in the `south_park` folder:

| File               | What it Does                                                             |
| ---                | ---                                                                      |
| `app.py`           | The main Python script where you initialize and pass data into your Flow |
| `Dockerfile`       | Lets you spin up a Docker instance running your app                      |
| `flows/`           | Folder to hold your Flows                                                |
| `pods/`            | Folder to hold your Pods                                                 |
| `README`           | The index to this tutorial                                               |
| `requirements.txt` | A list of requirements for `pip`                                         |

In the `flows/` folder we can see `index.yml` and `query.yml` - these define the indexing and querying Flows for your app.

In `pods/` we see `chunk.yml`, `craft.yml`, `doc.yml`, and `encode.yml` - these Pods are called from the Flows to process data for indexing or querying.

### Install Requirements

In your terminal:

```
cd south_park
pip install -r requirements.txt
```

All done? Now we can start editing these files to index and query our South Park data!

<table width="100%">
  <tr>
    <td>
      <strong><a href="../README.md">⬅️ Previous: README</a></strong>
    </td>
    <td align="right" style="text-align:right">
      <strong><a href="./run.md">Next: Running your app ➡️</a></strong>
    </td>
  </tr>
</table>
