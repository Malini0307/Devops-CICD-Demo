import { render, screen } from "@testing-library/react";
import App from "./App";

test("renders employee registration heading", () => {
  render(<App />);
  expect(
    screen.getByText(/Employee Registration/i)
  ).toBeInTheDocument();
});

test("renders employee name input", () => {
  render(<App />);
  expect(
    screen.getByPlaceholderText(
      "Enter Employee Name"
    )
  ).toBeInTheDocument();
});

test("renders email input", () => {
  render(<App />);
  expect(
    screen.getByPlaceholderText(
      "Enter Email"
    )
  ).toBeInTheDocument();
});

test("renders register button", () => {
  render(<App />);
  expect(
    screen.getByRole("button", {
      name: /Register/i,
    })
  ).toBeInTheDocument();
});