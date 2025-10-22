import streamlit as st
st.set_page_config("Ejemplo1_streamlit",page_icon="👇")
st.title("------BOLETA------")
st.markdown("Visita nuestra pagina oficial:[Escuela global](https://www.especializacionesglobal.net/)")
st.caption("Escuela global")
importe= st.number_input("Ingrese el monto de la venta",min_value=0,step=1)

if st.button("Generar"):
    st.caption("Generando boleta...")
    if importe == 0:
        st.caption("Por favor ingrese un valor positivo")
    else:
        valor_venta=importe/1.18
        igv=valor_venta*0.18
        st.subheader("Boleta venta")
        st.write("-------")  
        st.write(f"Operación Gravada: $ {valor_venta:.2f}")
        st.write(f"IGV: ${igv:.2f}")
        st.write(f"Importe Total: $ {importe:.2f} ")         
        st.write("-------")

st.markdown ("""
Detalles
Términos y condiciones:
- La presente boleta no es transferible
- No hay modificaciones de fechas y montos
""")
