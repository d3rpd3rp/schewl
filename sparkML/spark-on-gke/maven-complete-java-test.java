// $example on:programmatic_schema$
import java.util.ArrayList;
import java.util.List;
// $example off:programmatic_schema$
// $example on:create_ds$
import java.util.Arrays;
import java.util.Collections;
import java.io.Serializable;
// $example off:create_ds$
// $example on:schema_inferring$
// $example on:programmatic_schema$
import org.apache.spark.api.java.JavaRDD;
import org.apache.spark.api.java.function.Function;
// $example off:programmatic_schema$
// $example on:create_ds$
import org.apache.spark.api.java.function.MapFunction;
// $example on:create_df$
// $example on:run_sql$
// $example on:programmatic_schema$
import org.apache.spark.sql.Dataset;
import org.apache.spark.sql.Row;
// $example off:programmatic_schema$
// $example off:create_df$
// $example off:run_sql$
import org.apache.spark.sql.Encoder;
import org.apache.spark.sql.Encoders;
// $example off:create_ds$
// $example off:schema_inferring$
import org.apache.spark.sql.RowFactory;
// $example on:init_session$
import org.apache.spark.sql.SparkSession;
// $example off:init_session$
// $example on:programmatic_schema$
import org.apache.spark.sql.types.DataTypes;
import org.apache.spark.sql.types.StructField;
import org.apache.spark.sql.types.StructType;
// $example on:untyped_ops$
// col("...") is preferable to df.col("...")
import static org.apache.spark.sql.functions.col;
public class JavaSparkSQL {
  // $example on:create_ds$
    public static class javaVectorRow implements Serializable {
        private int quarter;
        private String stock;
        private String date;
        private Float open;
        private Float high;
        private Float low;
        private Float close;
        private Float volume;
        private Float percent_change_price;
        private Float percent_change_volume_over_last_wk;
        private Float previous_weeks_volume;
        private Float next_weeks_open;
        private Float next_weeks_close;
        private Float percent_change_next_weeks_price;
        private Float days_to_next_dividend;
        private Float percent_return_next_dividend;    
        }
    public static void main(String[] args) {
        // $example on:init_session$
        SparkSession spark = SparkSession
        .builder()
        .appName("Java Spark SQL Query MySQL Database & Write Java DataFrames")
        .getOrCreate();
        
        //spark.sql("SET -v").show(200, false);
        //spark.stop();
    }
}