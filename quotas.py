TEAM_QUOTA = {
    "vision-china": 128,
    "nlp-us": 256
}


def check_quota(config):
    team = config["team"]
    gpus = config["gpus"]

    if gpus > TEAM_QUOTA.get(team, 0):
        raise Exception(f"Quota exceeded for {team}")
