import {
  ResponsiveContainer,
  BarChart,
  Bar,
  CartesianGrid,
  Tooltip,
  XAxis,
  YAxis,
} from "recharts";

interface ItemSales {
  item: string;
  sales: number;
}

interface ItemChartProps {
  data: ItemSales[];
}

export default function ItemChart({
  data,
}: ItemChartProps) {
  return (
    <div className="rounded-xl bg-white p-6 shadow-md">

      <h2 className="mb-6 text-xl font-semibold text-gray-800">
        Top Selling Items
      </h2>

      <ResponsiveContainer
        width="100%"
        height={400}
      >
        <BarChart
          layout="vertical"
          data={data}
          margin={{
            top: 10,
            right: 20,
            left: 20,
            bottom: 10,
          }}
        >

          <CartesianGrid strokeDasharray="3 3" />

          <XAxis type="number" />

          <YAxis
            type="category"
            dataKey="item"
            width={80}
          />

          <Tooltip />

          <Bar
            dataKey="sales"
            fill="#10b981"
            radius={[0, 6, 6, 0]}
          />

        </BarChart>
      </ResponsiveContainer>

    </div>
  );
}
