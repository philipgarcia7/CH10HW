from pickle import TRUE
import ProcedureClass as pr
import PatientClass as pa

pat = pa.Patient(1, "Matt Jones", "123 Main st, Waco TX 76706", "254-555-7415", TRUE)

proc1 = pr.Procedure("Physical Exam", "2/15/2022", "Dr.Irvine", 250, 1)
proc2 = pr.Procedure("MRI", "2/15/2022", "Dr.Hamilton", 1500, 1)
proc3 = pr.Procedure("CT Scan", "2/17/2022", "Dr.Drey", 1200, 2)

print("*** Patient Bill ***")
print()
print("Name:", pat.get_name())
print("Address:", pat.get_address())
print("Phone:", pat.get_phone())
print()
print("Procedure:", proc1.get_name())
print("Date:", proc1.get_date())
print("Practitioner:", proc1.get_practitioner())
print("Charge: $", float(proc1.get_charge()))
print()
print("Procedure:", proc2.get_name())
print("Date:", proc2.get_date())
print("Practitioner:", proc2.get_practitioner())
print("Charge: $", float(proc2.get_charge()))


tc = proc1.get_charge() + proc2.get_charge()
if pat.get_veteran_status() == TRUE:
    discount = tc * 0.40
    tc -= discount


print()
print("Total Charges: $", format(tc, ",.2f"))
