import axios from "axios";

/**
 * Analytics response returned by FastAPI.
 */
export interface AnalyticsResponse {
  average_sales: number;
  total_sales: number;
  max_sales: number;
  min_sales: number;

  monthly_sales: {
    month: string;
    sales: number;
  }[];

  weekly_sales: {
    week: string;
    sales: number;
  }[];

  store_sales: {
    store: string;
    sales: number;
  }[];

  item_sales: {
    item: string;
    sales: number;
  }[];

  heatmap: {
    date: string;
    count: number;
  }[];
}

/**
 * FastAPI endpoint.
 */
const API_URL =
  "http://127.0.0.1:8000/analytics";

/**
 * Fetch analytics from backend.
 */
export async function getAnalytics():
Promise<AnalyticsResponse> {

  try {

    const response =
      await axios.get<AnalyticsResponse>(
        API_URL,
      );

    return response.data;

  } catch (error) {

    console.error(
      "Analytics request failed:",
      error,
    );

    throw new Error(
      "Unable to load analytics.",
    );

  }
}
