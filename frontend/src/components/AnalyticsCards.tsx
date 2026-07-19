interface AnalyticsCardsProps {
  averageSales: number;
  totalSales: number;
  maxSales: number;
  minSales: number;
}

export default function AnalyticsCards({
  averageSales,
  totalSales,
  maxSales,
  minSales,
}: AnalyticsCardsProps) {
  const cards = [
    {
      title: "Average Sales",
      value: averageSales.toFixed(2),
      color: "bg-blue-500",
    },
    {
      title: "Total Sales",
      value: totalSales.toLocaleString(),
      color: "bg-green-500",
    },
    {
      title: "Maximum Sales",
      value: maxSales.toString(),
      color: "bg-purple-500",
    },
    {
      title: "Minimum Sales",
      value: minSales.toString(),
      color: "bg-red-500",
    },
  ];

  return (
    <div className="grid gap-6 md:grid-cols-2 xl:grid-cols-4">
      {cards.map((card) => (
        <div
          key={card.title}
          className="rounded-xl bg-white p-6 shadow-md transition hover:shadow-lg"
        >
          <div
            className={`mb-4 h-2 rounded-full ${card.color}`}
          />

          <h3 className="text-sm text-gray-500">
            {card.title}
          </h3>

          <p className="mt-2 text-3xl font-bold text-gray-800">
            {card.value}
          </p>
        </div>
      ))}
    </div>
  );
}
