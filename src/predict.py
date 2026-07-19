from src.features.history import HistoryLookup
from src.services.model_service import ModelService

class Predictor:

    
    def __init__(self):

        self.lookup = HistoryLookup()

        self.service = ModelService()

    def predict(
        self,
        date,
        store,
        item,
    ):

        X = self.lookup.build_features(
            date=date,
            store=store,
            item=item,
        )

        prediction = self.service.predict(X)

        return prediction[0]
    
if __name__ == "__main__":

    predictor = Predictor()

    prediction = predictor.predict(
        date="2018-01-01",
        store=1,
        item=1,
    )

    print(f"Predicted Sales: {prediction:.2f}")