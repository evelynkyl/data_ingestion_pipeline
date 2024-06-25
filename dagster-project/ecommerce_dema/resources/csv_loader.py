from io import StringIO

from dagster import get_dagster_logger, ConfigurableResource
import requests
import pandas as pd

logger = get_dagster_logger()


class CsvLoaderResource(ConfigurableResource):
    @staticmethod
    def load_csv_to_dataframe(url: str) -> pd.DataFrame or None:
        """
        Fetches a CSV file from the given URL and loads it into a pandas DataFrame.

        Args:
        - url (str): The URL from which to fetch the CSV file.

        Returns:
        - pd.DataFrame: A pandas DataFrame containing the CSV data, or None if an error occurs.

        Raises:
        - ValueError: If the URL is invalid or the response status code is not 200.
        - requests.exceptions.RequestException: If there is an error during the request.

        """
        try:
            response = requests.get(url)
            response.raise_for_status()
            csv_content = response.text
            df = pd.read_csv(StringIO(csv_content))
            return df
        except requests.exceptions.RequestException as e:
            logger.error(f"Error fetching data from {url}: {e}")
            return None
        except pd.errors.EmptyDataError as e:
            logger.error(f"Error loading CSV data from {url}: {e}")
            return None
        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            return None
