#include <good.hpp>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <pybind11/complex.h>
#include <pybind11/chrono.h>

namespace py = pybind11;
using namespace TradingSpace;

//! Create a new module called good
PYBIND11_MODULE(good, m) {
  m.doc() = "Good";
  
  py::class_<Good>(m, "Good")
  .def(py::init<int, std::string, float, float, float, float>())
  .def("set_value", &Good::set_value)
  .def("get_value", &Good::get_value)
  .def("get_name", &Good::get_name)
  .def("get_id", &Good::get_id)
  .def("adapat", &Good::adapt)
  .def("operator<", &Good::operator<)
  .def("operator==", &Good::operator==);


}
