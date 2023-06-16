# Snoop Dogg Zen Quote Plugin

## Background
Ok, so I needed some ideas for my first ChatGPT plugin, so I went to ChatGPT and it gave me a few - https://chat.openai.com/share/a6c389b6-31f1-4e46-8bd0-c725f2d1098a

Based upon one its recommendations (a joke plugin)...I thought of the idea to create a Confucius quote in the style of Snoop Dogg type of plugin. The idea would be that if someone needed some wisdom...who better than Snoop D-O-G-G to give em some.

However, after a bit of searching, getting an api for confucius quotes was proving to be difficult...so I pivoted and went with an alternative...zen style quotes using the Zen Quotes api.

And thus was born the Snoop Zen Quote ChatGPT plugin.

## The Build
First, I'm using the [Zen Quotes API](https://zenquotes.io/). It's free and doesn't require authentication...which made it a perfect candidate for a simple ChatGPT plugin. [OpenAI](https://platform.openai.com/docs/plugins/examples) provides great documentation on how to build plugins so put together a simple Python/Flask app that hits up the Zen Quotes api, Snoopify's it a bit (yeah, it rudimentary) and returns back the quote.

Second, the plugin is made up of a couple of python app files (main.py, snoopify.py), a plugin manifest file (ai-plugin.json), and an OpenAI definition file (openapi.yaml).

Third, for testing and serving my plugin for consumption in ChatGPT, I decided to use [Replit](https://replit.com/)...which is a phenomenal service. Easy to get started with and handles code storage and plugin serving. Replit does way more than that and I definitely recommend trying out all the goodness that Replit has.
