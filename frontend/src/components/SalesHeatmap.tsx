import CalendarHeatmap from "react-calendar-heatmap";
import "react-calendar-heatmap/dist/styles.css";

interface HeatmapData {
  date: string;
  count: number;
}

interface SalesHeatmapProps {
  data: HeatmapData[];
}

export default function SalesHeatmap({
  data,
}: SalesHeatmapProps) {
  return (
    <div className="rounded-xl bg-white p-6 shadow-md">

      <h2 className="mb-6 text-xl font-semibold text-gray-800">
        Sales Activity Heatmap
      </h2>

      <CalendarHeatmap
        startDate={new Date("2017-01-01")}
        endDate={new Date("2017-12-31")}
        values={data}
        classForValue={(value) => {
          if (!value) return "color-empty";

          if (value.count >= 80)
            return "color-github-4";

          if (value.count >= 60)
            return "color-github-3";

          if (value.count >= 40)
            return "color-github-2";

          if (value.count >= 20)
            return "color-github-1";

          return "color-empty";
        }}
        showWeekdayLabels
      />

    </div>
  );
}
