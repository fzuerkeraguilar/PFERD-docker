# PFERD-docker
Dockerized version of [PFERD](https://github.com/Garmelon/PFERD/) with cron support

## Usage 
The execution of PFERD is set by the `CRON_SCHEDULE` envoirement variable.
PFERD is executed one time at startup and then follows the provided cron schedule.
PFERD is set to use `/pferd/pferd.cfg` as the config file and `/pferd/working-dir` as the working directory.
The Logs of PFERD are appended to /pferd/pferd.logrun
### docker cli example
```bash
docker run -d \
    --name=pferd \
    -e CRON_SCHEDULE="0 1 * * *" \
    -v /path/to/config.cfg=/pferd/pferd.cfg \
    -v /path/to/working-dir=/pferd/working-dir \
    --restart unless-stopped
    fzuerkeraguilar/pferd:latest
```
