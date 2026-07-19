import {
  Area,
  AreaChart,
  CartesianGrid,
  ResponsiveContainer,
  Tooltip,
  XAxis,
  YAxis,
} from "recharts";

interface WeeklySales {
  week: string;
  sales: number;
}

interface WeeklySalesChartProps {
  data: WeeklySales[];
}

export default function WeeklySalesChart({
  data,
}: WeeklySalesChartProps) {
  return (
    <div className="rounded-xl bg-white p-6 shadow-md">

      <h2 className="mb-6 text-xl font-semibold text-gray-800">
        Weekly Sales Trend
      </h2>

      <ResponsiveContainer
        width="100%"
        height={350}
      >
        <AreaChart data={data}>

          <CartesianGrid strokeDasharray="3 3" />

          <XAxis dataKey="week" />

          <YAxis />

          <Tooltip />

          <Area
            type="monotone"
            dataKey="sales"
            stroke="#10b981"
            fill="#6ee7b7"
            strokeWidth={3}
          />

        </AreaChart>
      </ResponsiveContainer>

    </div>
  );
}
