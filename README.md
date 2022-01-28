# Timed messages

For Discord webhooks or anything that requires time.

`noon-progress.py` sends a message at noon at the machine's time, showing how much of the year has passed.

## Setting up

1. Create a [Discord webhook](https://support.discord.com/hc/articles/228383668).
1. Create `config.py` in the same folder as `noon-progress.py`. Paste in the following code and replace URL with the link of the Discord webhook. This will be the webhook that will be used.
    ```python
    webhook_url = 'URL'
    ```
1. Run the code daily. On Linux, [cron jobs](https://www.freecodecamp.org/news/cron-jobs-in-linux/) can be used.

## Ideas for future development
* Filled icon showing how much of the year is over
* Scheduling message to be sent, rather than `time.sleep()`

## Acknowledgements

Inspired by [@ProgressBar202_](https://twitter.com/ProgressBar202_) on Twitter