#include <account.hpp>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <pybind11/complex.h>
#include <pybind11/chrono.h>

namespace py = pybind11;
using namespace TradingSpace;

//! Create a new module called account
PYBIND11_MODULE(account, m) {
  m.doc() = "Account";
  
  py::class_<Account>(m, "Account")
  .def(py::init<>())
  .def("withdraw", &Account::withdraw)
  .def("deposit", &Account::deposit)
  .def("get_balance", &Account::get_balance)
  .def("set_balance", &Account::set_balance);

}
