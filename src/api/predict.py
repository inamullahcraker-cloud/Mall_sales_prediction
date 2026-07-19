def predict_single(
    self,
    date,
    store,
    item,
):
    """
    Predict sales for one store-item-date.
    """

    return self.history_lookup.predict(

        date=date,

        store=store,

        item=item,

        model_service=self.service,

    )