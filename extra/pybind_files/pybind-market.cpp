#include <market.hpp>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <pybind11/complex.h>
#include <pybind11/chrono.h>

namespace py = pybind11;
using namespace TradingSpace;

PYBIND11_MODULE(market, m) {
  m.doc() = "Market";
  
  py::class_<Market>(m, "Market")
  .def(py::init<>())
  .def("addTrader", &Market::addTrader)
  .def("removeTrader", &Market::removeTrader)
  .def("removeTraderById", &Market::removeTraderById)
  .def("update_values", &Market::update_values)
  .def("get_traders", &Market::get_traders)
  .def("get_goods", &Market::get_goods)
  .def("set_trader_password", &Market::set_trader_password)
  .def("get_trader_by_id", &Market::get_trader_by_id);
}
