from typing import Callable, List, Self, TypeVar
from pyspark import SparkContext, SparkConf
import pyspark

T = TypeVar("T")


class APriori:
    def __init__(self, app_name="APriori Example", master_url="local", bind_address="localhost", bind_port="4050"):
        self.threshold: int = None
        self.candidate_set: List[List[T]] = []

        configuration = SparkConf().setAppName(app_name).setMaster(master_url).set(
            "spark.driver.bindAddress", bind_address).set("spark.ui.port", bind_port)
        self.spark_session: SparkContext | None = SparkContext(
            appName=app_name, conf=configuration).getOrCreate()

    def read_data(self, file_path) -> Self:
        self.data = None
        return self

    def set_support_threshold(self, threshold: int) -> Self:
        self.threshold = threshold
        return self

    def set_candidate_set(self, candidates: List[T]) -> Self:
        self.candidate_set = candidates
        return self

    def prune_candidates(self) -> Self:
        for each_item in self.candidate_set:
            for _, row in self.data.iterrows():
                pass
        return self

    def debug(self) -> Self:
        return self


if __name__ == '__main__':

    apriori = APriori().read_data(
        './data/supermarket_sales.csv')
