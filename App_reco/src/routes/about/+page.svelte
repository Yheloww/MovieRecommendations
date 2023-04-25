<!-- test with movie db -->
<script context="module">
    export async function load({ fetch }){
        const res = await fetch(
            'https://api.themoviedb.org/3/movie/550?api_key=0f19c042aac4b96dd9c50c70ff491332'
        );
        const data = await res.json();
        if (res.ok){
            return {
                props: { popular: data.results }
            };
        }
    }
</script>