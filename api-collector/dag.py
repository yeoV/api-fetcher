from airflow.decorators import dag, task


@dag(dag_id="api-caller", render_template_as_native_obj=True)
def main():
    pass


main()
