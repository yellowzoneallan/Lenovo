import argparse
import yaml
from router import route_job


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", required=True)
    args = parser.parse_args()

    with open(args.config) as f:
        config = yaml.safe_load(f)

    result = route_job(config)
    print(result)


if __name__ == "__main__":
    main()
