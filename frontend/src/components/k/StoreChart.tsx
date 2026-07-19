import {
  ResponsiveContainer,
  BarChart,
  Bar,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
} from "recharts";

interface StoreSales {
  store: string;
  sales: number;
}

interface StoreChartProps {
  data: StoreSales[];
}

export default function StoreChart({
  data,
}: StoreChartProps) {
  return (
    <div className="rounded-xl bg-white p-6 shadow-md">

      <h2 className="mb-6 text-xl font-semibold text-gray-800">
        Store Comparison
      </h2>

      <ResponsiveContainer
        width="100%"
        height={350}
      >
        <BarChart data={data}>

          <CartesianGrid strokeDasharray="3 3" />

          <XAxis dataKey="store" />

          <YAxis />

          <Tooltip />

          <Bar
            dataKey="sales"
            fill="#3b82f6"
            radius={[6, 6, 0, 0]}
          />

        </BarChart>
      </ResponsiveContainer>

    </div>
  );
}
