#include <account.hpp>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <pybind11/complex.h>
#include <pybind11/chrono.h>

namespace py = pybind11;
using namespace TradingSpace;

PYBIND11_MODULE(account, m) {
  m.doc() = "Account";
  
  py::class_<Account>(m, "Account")
  .def(py::init<>())
  .def(py::init<const float&>())
  .def("withdraw", &Account::withdraw)
  .def("deposit", &Account::deposit)
  .def("get_balance", &Account::get_balance)
  .def("set_balance", &Account::set_balance);

}