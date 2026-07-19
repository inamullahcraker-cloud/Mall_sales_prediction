import {
  LineChart,
  Line,
  CartesianGrid,
  Tooltip,
  ResponsiveContainer,
  XAxis,
  YAxis,
} from "recharts";

interface MonthlySales {
  month: string;
  sales: number;
}

interface MonthlySalesChartProps {
  data: MonthlySales[];
}

export default function MonthlySalesChart({
  data,
}: MonthlySalesChartProps) {
  return (
    <div className="rounded-xl bg-white p-6 shadow-md">

      <h2 className="mb-6 text-xl font-semibold text-gray-800">
        Monthly Sales Trend
      </h2>

      <ResponsiveContainer
        width="100%"
        height={350}
      >
        <LineChart data={data}>

          <CartesianGrid strokeDasharray="3 3" />

          <XAxis dataKey="month" />

          <YAxis />

          <Tooltip />

          <Line
            type="monotone"
            dataKey="sales"
            stroke="#2563eb"
            strokeWidth={3}
            dot={{ r: 5 }}
            activeDot={{ r: 8 }}
          />

        </LineChart>
      </ResponsiveContainer>

    </div>
  );
}
