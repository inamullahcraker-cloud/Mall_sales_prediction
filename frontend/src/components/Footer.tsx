/**
 * Footer component.
 *
 * Displays project information
 * and technologies used.
 */

function Footer() {
  return (
    <footer className="mt-12 border-t bg-white">

      <div className="mx-auto flex max-w-6xl flex-col items-center justify-between gap-4 px-6 py-6 md:flex-row">

        <div>
          <p className="text-sm text-gray-600">
            © 2026 Inamullah
          </p>

          <p className="text-sm text-gray-500">
            Store Item Sales Forecasting
          </p>
        </div>

        <div className="flex flex-wrap justify-center gap-2">

          <span className="rounded-full bg-blue-100 px-3 py-1 text-sm font-medium text-blue-700">
            React
          </span>

          <span className="rounded-full bg-cyan-100 px-3 py-1 text-sm font-medium text-cyan-700">
            TypeScript
          </span>

          <span className="rounded-full bg-green-100 px-3 py-1 text-sm font-medium text-green-700">
            FastAPI
          </span>

          <span className="rounded-full bg-yellow-100 px-3 py-1 text-sm font-medium text-yellow-700">
            Scikit-Learn
          </span>

          <span className="rounded-full bg-purple-100 px-3 py-1 text-sm font-medium text-purple-700">
            XGBoost
          </span>

        </div>

      </div>

    </footer>
  );
}

export default Footer;
