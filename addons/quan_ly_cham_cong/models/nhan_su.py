from odoo import models, fields, api


class NhanSu(models.Model):
    _name = 'nhan_su'
    _description = 'Bảng chứa thông tin nhân sự'
    _rec_name = "ten_nhan_su"

    ma_dinh_danh = fields.Char("Mã định danh", required=True)
    ten_nhan_su = fields.Char("Tên nhân viên", required=True)
    dien_thoai = fields.Char("Số điện thoại", required=True)
    trang_thai = fields.Selection([
        ("Đang làm việc", "Đang làm việc"),
        ("Nghĩ việc", "Nghỉ việc"),
    ], string= "Trạng thái", default = "Đang làm việc")    