import {
  LineChart,
  Line,
  CartesianGrid,
  Tooltip,
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

      <h2 className="mb-6 text-xl font-semibold">
        Monthly Sales
      </h2>

      <LineChart
        width={900}
        height={350}
        data={data}
      >
        <CartesianGrid strokeDasharray="3 3" />
        <XAxis dataKey="month" />
        <YAxis />
        <Tooltip />
        <Line
          dataKey="sales"
          stroke="#2563eb"
        />
      </LineChart>

    </div>
  );
}
