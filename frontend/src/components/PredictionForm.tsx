import { useState } from "react";

import { predictSales } from "../api/prediction";

interface PredictionFormProps {
  onPrediction: (sales: number) => void;
}

function PredictionForm({
  onPrediction,
}: PredictionFormProps) {
  const [date, setDate] = useState("");

  const [store, setStore] = useState(1);

  const [item, setItem] = useState(1);

  const [loading, setLoading] = useState(false);

  const [error, setError] = useState("");

  const handleSubmit = async (
    event: React.FormEvent,
  ) => {
    event.preventDefault();

    setError("");

    if (!date) {
      setError("Please select a date.");
      return;
    }

    try {
      setLoading(true);

      const response = await predictSales({
        date,
        store,
        item,
      });

      onPrediction(
        response.predicted_sales,
      );
    } catch {
      setError(
        "Prediction failed. Please try again."
      );
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="rounded-xl bg-white p-8 shadow">

      <h2 className="mb-6 text-2xl font-semibold">
        Predict Sales
      </h2>

      <form
        onSubmit={handleSubmit}
        className="space-y-5"
      >
        <div>
          <label className="mb-2 block font-medium">
            Date
          </label>

          <input
            type="date"
            value={date}
            onChange={(e) =>
              setDate(e.target.value)
            }
            className="w-full rounded-lg border p-3"
          />
        </div>

        <div>
          <label className="mb-2 block font-medium">
            Store
          </label>

          <input
            type="number"
            min={1}
            value={store}
            onChange={(e) =>
              setStore(
                Number(e.target.value)
              )
            }
            className="w-full rounded-lg border p-3"
          />
        </div>

        <div>
          <label className="mb-2 block font-medium">
            Item
          </label>

          <input
            type="number"
            min={1}
            value={item}
            onChange={(e) =>
              setItem(
                Number(e.target.value)
              )
            }
            className="w-full rounded-lg border p-3"
          />
        </div>

        {error && (
          <p className="text-red-600">
            {error}
          </p>
        )}

        <button
          type="submit"
          disabled={loading}
          className="w-full rounded-lg bg-blue-600 py-3 font-semibold text-white transition hover:bg-blue-700 disabled:bg-gray-400"
        >
          {loading
            ? "Predicting..."
            : "Predict Sales"}
        </button>
      </form>
    </div>
  );
}

export default PredictionForm;
