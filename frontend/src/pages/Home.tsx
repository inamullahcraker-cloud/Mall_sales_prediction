import { useState } from "react";

import Header from "../components/Header";
import PredictionForm from "../components/PredictionForm";
import PredictionResult from "../components/PredictionResult";
import Footer from "../components/Footer";

function Home() {
  const [prediction, setPrediction] = useState<number | null>(
    null,
  );

  return (
    <div className="min-h-screen bg-slate-100">

      <Header />

      <main className="mx-auto max-w-6xl px-6 py-10">

        <div className="grid gap-8 lg:grid-cols-2">

          <PredictionForm
            onPrediction={setPrediction}
          />

          <PredictionResult
            sales={prediction}
          />

        </div>

      </main>

      <Footer />



    </div>
  );
}

export default Home;
