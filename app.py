import streamlit as st

# Cấu hình giao diện trang web
st.set_page_config(
    page_title="Tính chỉ số DTI (Debt-to-Income)",
    page_icon="💰",
    layout="centered"
)

st.title("Ứng dụng tính toán và đánh giá chỉ số DTI")
st.write("Vui lòng nhập các thông tin tài chính của bạn bên dưới để kiểm tra khả năng được duyệt khoản vay:")

# Form nhập liệu
with st.form("dti_form"):
    col1, col2 = st.columns(2)
    
    with col1:
        stv = st.number_input(
            "Số tiền vay (STV - VNĐ)", 
            min_value=0.0, 
            value=800_000_000.0, 
            step=10_000_000.0, 
            format="%.0f"
        )
        thv = st.number_input(
            "Thời hạn vay (THV - năm)", 
            min_value=1.0, 
            value=5.0, 
            step=1.0
        )
        ls = st.number_input(
            "Lãi suất vay (LS - tỷ lệ năm)", 
            min_value=0.0, 
            max_value=1.0, 
            value=0.12, 
            step=0.01, 
            format="%.2f"
        )
        tn = st.number_input(
            "Thu nhập hàng tháng (TN - VNĐ)", 
            min_value=0.0, 
            value=45_000_000.0, 
            step=1_000_000.0, 
            format="%.0f"
        )
        
    with col2:
        nc = st.number_input(
            "Nợ cũ hàng tháng (NC - VNĐ)", 
            min_value=0.0, 
            value=10_000_000.0, 
            step=1_000_000.0, 
            format="%.0f"
        )
        cpsh = st.number_input(
            "Chi phí sinh hoạt 1 người/tháng (CPSH - VNĐ)", 
            min_value=0.0, 
            value=4_000_000.0, 
            step=500_000.0, 
            format="%.0f"
        )
        sn = st.number_input(
            "Số người trong gia đình (SN)", 
            min_value=1, 
            value=3, 
            step=1
        )

    submitted = st.form_submit_button("Tính toán và Đánh giá DTI")

if submitted:
    # Kiểm tra mẫu số để tránh lỗi chia cho 0 hoặc số âm
    mau_so = tn - (cpsh * sn)
    
    if mau_so <= 0:
        st.error("Lỗi: Thu nhập không đủ trang trải chi phí sinh hoạt của gia đình (Thu nhập - Chi phí sinh hoạt <= 0).")
    else:
        # Tính toán chỉ số DTI theo công thức gốc
        dti = ((stv / (thv * 12) + stv * (ls / 12)) + nc) / mau_so
        
        st.markdown("---")
        st.subheader("Kết quả phân tích")
        
        res_col1, res_col2 = st.columns(2)
        
        with res_col1:
            st.metric(label="Chỉ số DTI tính được", value=f"{dti:.2%}")
            
        with res_col2:
            # Logic theo code mẫu của bạn: DTI < 0.7 là ĐƯỢC VAY
            # (Nếu muốn đổi ngược lại thành DTI < 70% là KHÔNG ĐƯỢC VAY, hãy đổi dấu < thành >=)
            if dti < 0.7:
                st.success("Kết quả: ĐƯỢC VAY")
            else:
                st.error("Kết quả: KHÔNG ĐƯỢC VAY")
                
        # Chi tiết thành phần tính toán
        with st.expander("Xem chi tiết các khoản phí hàng tháng"):
            goc_hang_thang = stv / (thv * 12)
            lai_hang_thang = stv * (ls / 12)
            tong_tra_no = goc_hang_thang + lai_hang_thang + nc
            
            st.write(f"- Tiền gốc phải trả hàng tháng: {goc_hang_thang:,.0f} VNĐ")
            st.write(f"- Tiền lãi ước tính hàng tháng: {lai_hang_thang:,.0f} VNĐ")
            st.write(f"- Tổng nghĩa vụ trả nợ (gốc + lãi + nợ cũ): {tong_tra_no:,.0f} VNĐ")
            st.write(f"- Thu nhập sau khi trừ chi phí sinh hoạt: {mau_so:,.0f} VNĐ")
