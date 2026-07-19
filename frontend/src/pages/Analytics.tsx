import { useCallback, useEffect, useState } from "react";
import { Link } from "react-router-dom";

import AnalyticsCards from "../components/AnalyticsCards";
import MonthlySalesChart from "../components/MonthlySalesChart";
import WeeklySalesChart from "../components/WeeklySalesChart";
import StoreChart from "../components/StoreChart";
import ItemChart from "../components/ItemChart";
import SalesHeatmap from "../components/SalesHeatmap";

import { getAnalytics } from "../api/analytics";
import type { AnalyticsResponse } from "../api/analytics";

export default function Analytics() {
  const [analytics, setAnalytics] =
    useState<AnalyticsResponse | null>(null);

  const [loading, setLoading] = useState(true);
  const [refreshing, setRefreshing] = useState(false);
  const [error, setError] = useState("");

  const fetchAnalytics = useCallback(
    async (isRefresh: boolean) => {
      try {
        if (isRefresh) {
          setRefreshing(true);
        } else {
          setLoading(true);
        }

        setError("");

        const data = await getAnalytics();
        setAnalytics(data);
      } catch (err) {
        console.error(err);
        setError("Unable to load analytics.");
      } finally {
        setLoading(false);
        setRefreshing(false);
      }
    },
    [],
  );

  useEffect(() => {
    fetchAnalytics(false);
  }, [fetchAnalytics]);

  const topBar = (
    <div className="mb-8 flex flex-wrap items-center justify-between gap-4">
      <Link
        to="/"
        className="flex items-center gap-2 rounded-lg bg-white px-4 py-2 text-sm font-medium text-gray-700 shadow transition hover:bg-gray-50"
      >
        <span aria-hidden="true">←</span>
        Back to Predict
      </Link>

      <button
        type="button"
        onClick={() => fetchAnalytics(true)}
        disabled={loading || refreshing}
        className="rounded-lg bg-blue-600 px-4 py-2 text-sm font-medium text-white shadow transition hover:bg-blue-700 disabled:bg-gray-400"
      >
        {refreshing ? "Refreshing..." : "Refresh Data"}
      </button>
    </div>
  );

  if (loading) {
    return (
      <div className="min-h-screen bg-gray-100 p-8">
        {topBar}

        <div className="flex h-[60vh] items-center justify-center text-xl text-gray-600">
          Loading Analytics...
        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="min-h-screen bg-gray-100 p-8">
        {topBar}

        <div className="flex h-[60vh] items-center justify-center text-xl text-red-500">
          {error}
        </div>
      </div>
    );
  }

  if (!analytics) {
    return null;
  }

  return (
    <div className="min-h-screen bg-gray-100 p-8">
      {topBar}

      <h1 className="mb-8 text-4xl font-bold text-gray-800">
        Sales Analytics
      </h1>

      <AnalyticsCards
        averageSales={analytics.average_sales}
        totalSales={analytics.total_sales}
        maxSales={analytics.max_sales}
        minSales={analytics.min_sales}
      />

      <div className="mt-8">
        <MonthlySalesChart data={analytics.monthly_sales} />
      </div>

      <div className="mt-8">
        <WeeklySalesChart data={analytics.weekly_sales} />
      </div>

      <div className="mt-8 grid gap-8 lg:grid-cols-2">
        <StoreChart data={analytics.store_sales} />
        <ItemChart data={analytics.item_sales} />
      </div>

      <div className="mt-8">
        <SalesHeatmap data={analytics.heatmap} />
      </div>
    </div>
  );
}

