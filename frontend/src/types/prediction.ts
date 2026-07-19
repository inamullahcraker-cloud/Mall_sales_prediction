export interface PredictionRequest {
  date: string;
  store: number;
  item: number;
}

export interface PredictionResponse {
  predicted_sales: number;
}
