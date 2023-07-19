frappe.ui.form.on("Student Group", {
  batch: function (frm) {
    if (frm.doc.batch) {
      const currentYear = new Date().getFullYear();
      const studentGroupName = `${frm.doc.batch}-${currentYear}`;
      frm.set_value("student_group_name", studentGroupName);
    }
  },
});
