import pandas as pd
import streamlit as st

st.title("Hierarchical Data Viewer")
st.header("this is a header")
st.subheader("subheader")
st.caption("caption")
st.write("this is write")
st.text("fixed text")
st.code("v = variable()\nanother_call()", "python")
st.markdown("*bold*")
st.divider()

st.latex("...")

st.error("this is an error")
st.info("this is an info")
st.warning("this is an warning")
st.success("this is an success")

st.balloons()
st.snow()