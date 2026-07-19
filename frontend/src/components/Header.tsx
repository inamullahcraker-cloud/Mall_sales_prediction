/**
 * Header component.
 *
 * Displays the application title,
 * short description, and page navigation.
 */

import { NavLink } from "react-router-dom";

function Header() {
  const linkClass = ({ isActive }: { isActive: boolean }) =>
    `rounded-lg px-4 py-2 text-sm font-medium transition ${
      isActive
        ? "bg-white text-blue-700"
        : "text-blue-100 hover:bg-blue-500 hover:text-white"
    }`;

  return (
    <header className="bg-blue-600 text-white shadow-md">
      <div className="mx-auto max-w-5xl px-6 py-8">
        <h1 className="text-4xl font-bold">
          Store Item Sales Forecasting
        </h1>

        <p className="mt-2 text-lg text-blue-100">
          Machine Learning Powered Demand Prediction
        </p>

        <nav className="mt-6 flex gap-2">
          <NavLink to="/" end className={linkClass}>
            Predict
          </NavLink>

          <NavLink to="/analytics" className={linkClass}>
            Analytics
          </NavLink>
        </nav>
      </div>
    </header>
  );
}

export default Header;
