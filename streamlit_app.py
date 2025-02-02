import streamlit as st


# Initialize connection.
conn = st.connection('mysql', type='sql')
#st.write(f"host: {st.secrets.connections.mysql.host}")

if conn:
# Perform query.
    df = conn.query('SELECT a.auction_date, a.buyer, count(distinct a.purchase_id) p_id_cnt , sum(l.lot_weight * a.auction_price) as total_price , sum(l.lot_weight * a.auction_price) * 0.07 commission , count(1) FROM prod_auction_database.auction_lot_data a inner join prod_auction_database.lot_data  l on l.purchase_id = a.purchase_id and l.item_name = a.item_name 		and l.lot_number = a.lot_number group by 1, 2  order by 1 desc limit 10;', ttl=600)
else:
    st.write(f"mysql conn not found")

# Print results.
for row in df.itertuples():
    st.write(f"{row.auction_date} has a :{row.buyer}:")
    
st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
