import streamlit as st

st.markdown("# :green[💪 Doung Café 🏋️]")
st.write("ยินดีต้อนรับเข้าสู่ :green[Doung Café] กรุณาเลือกสินค้าของคุณ")
st.write("Welcome to :green[Doung Café] Please select your order")
Espresso_count = st.number_input('Espresso เอสเพรสโซ (แก้ว)' ,value = 0)
Americano_count = st.number_input('Americano อเมริกาโน (แก้ว)' ,value = 0)
Latte_count = st.number_input('Latte ลาเต้ (แก้ว)' ,value = 0)
Cappuccino_count = st.number_input('Cappuccino คาปูชิโน (แก้ว)' ,value = 0)
Mocha_count = st.number_input('Mocha มอคค่า (แก้ว)' ,value = 0)
IcedCoffee_count = st.number_input('Iced Coffee กาแฟเย็น (แก้ว)' ,value = 0)
count_sum = IcedCoffee_count + Mocha_count + Cappuccino_count + Latte_count + Americano_count + Espresso_count
if Espresso_count or Americano_count or Latte_count or Cappuccino_count or Mocha_count or IcedCoffee_count >= 0:
  st.write(f'จำนวนสินค้า {count_sum}')
else st.write(':red[Error: จำนวนสินค้าไม่สามารถติดลบได้]')

#st.write("Welcome to :green[Doung Café] Please select your order")
