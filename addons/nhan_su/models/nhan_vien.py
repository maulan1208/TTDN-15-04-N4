from odoo import models, fields, api
from datetime import date

class NhanVien(models.Model):
    _name = 'nhan_vien'
    _description = 'Bảng chứa thông tin nhân viên'

    ma_dinh_danh = fields.Char("Mã định danh", required=True)
    ngay_sinh = fields.Date("Ngày sinh")
    que_quan = fields.Char("Quê quán")
    email = fields.Char("Email")
    so_dien_thoai = fields.Char("Số điện thoại")
    lich_su_cong_tac_id = fields.One2many("lich_su_cong_tac", string="Danh sách lịch sử công tác", inverse_name="nhan_vien_id")

    ho_ten_dem = fields.Char("Họ tên đệm", requited = True)
    ten = fields.Char("Tên", requited = True)
    ho_va_ten = fields.Char("Họ và tên", compute = "_tinh_ho_va_ten", store = True)

    # tuoi = fields.Date("Tuổi", compute = "_tinh_tuoi", store = True)

    @api.depends("ho_ten_dem", "ten")
    def _tinh_ho_va_ten(seft):
        for record in seft:
            if record.ho_ten_dem and record.ten:
                record.ho_va_ten = record.ho_ten_dem + ' ' + record.ten

    # @api.depends("ngay_sinh")
    # def _tinh_tuoi(seft):
    #     today = date.today()
    #     for record in seft:
    #         if record.ngay_sinh:
    #             ngay_sinh = 
    #             record.tuoi = today.year - 