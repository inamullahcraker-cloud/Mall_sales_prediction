import axios from "axios";

import type {
  PredictionRequest,
  PredictionResponse,
} from "../types/prediction";

const API_URL = "http://127.0.0.1:8000/predict";

export async function predictSales(
  data: PredictionRequest,
): Promise<PredictionResponse> {
  try {
    const response = await axios.post<PredictionResponse>(
      API_URL,
      data,
      {
        headers: {
          "Content-Type": "application/json",
        },
      },
    );

    return response.data;
  } catch (error) {
    console.error("Prediction failed:", error);

    throw new Error(
      "Unable to connect to the prediction service.",
    );
  }
}
