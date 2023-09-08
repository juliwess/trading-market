#include <trader.hpp>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <pybind11/complex.h>
#include <pybind11/chrono.h>

namespace py = pybind11;
using namespace TradingSpace;

PYBIND11_MODULE(trader, m) {
  m.doc() = "Trader";
  
  py::class_<Trader>(m, "Trader")
  .def(py::init<>())
  .def("buy", &Trader::buy)
  .def("sell", &Trader::sell)
  .def("set_balance", &Trader::set_balance)
  .def("deposit", &Trader::deposit)
  .def("withdraw", &Trader::withdraw)
  .def("validate", &Trader::validate)
  .def("get_account", &Trader::get_account)
  .def("set_account", &Trader::set_account)
  .def("get_id", &Trader::get_id)
  .def("set_id", &Trader::set_id)
  .def("get_instances", &Trader::get_instances)
  .def("get_traders_goods", &Trader::get_traders_goods)
  .def("get_pw", &Trader::get_pw)
  .def("set_pw", &Trader::set_pw)
  .def("operator==", &Trader::operator==);

}
