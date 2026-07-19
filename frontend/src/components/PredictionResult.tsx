interface PredictionResultProps {
  sales: number | null;
}

function PredictionResult({
  sales,
}: PredictionResultProps) {
  if (sales === null) {
    return (
      <div className="rounded-xl bg-white p-8 text-center shadow">
        <h2 className="text-2xl font-semibold">
          Prediction Result
        </h2>

        <p className="mt-4 text-gray-500">
          Enter a date, store, and item to predict sales.
        </p>
      </div>
    );
  }

  return (
    <div className="rounded-xl bg-white p-8 text-center shadow">

      <h2 className="text-2xl font-semibold">
        Predicted Sales
      </h2>

      <p className="mt-6 text-6xl font-bold text-blue-600">
        {sales.toFixed(2)}
      </p>

      <p className="mt-3 text-lg text-gray-600">
        Units
      </p>

    </div>
  );
}

export default PredictionResult;
