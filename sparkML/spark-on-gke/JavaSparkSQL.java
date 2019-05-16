/*
 * https://github.com/apache/spark/blob/master/examples/src/main/java/org/apache/spark/examples/sql/JavaSparkSQLExample.java
 * Licensed to the Apache Software Foundation (ASF) under one or more
 * contributor license agreements.  See the NOTICE file distributed with
 * this work for additional information regarding copyright ownership.
 * The ASF licenses this file to You under the Apache License, Version 2.0
 * (the "License"); you may not use this file except in compliance with
 * the License.  You may obtain a copy of the License at
 *
 *    http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

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
// $example off:programmatic_schema$
import org.apache.spark.sql.AnalysisException;

// $example on:untyped_ops$
// col("...") is preferable to df.col("...")
import static org.apache.spark.sql.functions.col;
// $example off:untyped_ops$

//simple date
import java.text.SimpleDateFormat;

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
    public String getquarter(){
        return quarter;
    }
    public String setquarter(){
        this.name = quarter;
    }
    public String getstock(){
        return stock;
    }
    public String setstock(){
        this.name = stock;
    }
    public String getdate(){
        return date;
    }
    public String setdate(){
        this.name = date;
    }
    public String getopen(){
        return open;
    }
    public String setopen(){
        this.name = open;
    }
    public String gethigh(){
        return high;
    }
    public String sethigh(){
        this.name = high;
    }
    public String getlow(){
        return low;
    }
    public String setlow(){
        this.name = low;
    }
    public String getclose(){
        return close;
    }
    public String setclose(){
        this.name = close;
    }
    public String getvolume(){
        return volume;
    }
    public String setvolume(){
        this.name = volume;
    }
    public String getpercent_change_price(){
        return percent_change_price;
    }
    public String setpercent_change_price(){
        this.name = percent_change_price;
    }
    public String getpercent_change_volume_over_last_wk(){
        return percent_change_volume_over_last_wk;
    }
    public String setpercent_change_volume_over_last_wk(){
        this.name = percent_change_volume_over_last_wk;
    }
    public String getprevious_weeks_volume(){
        return previous_weeks_volume;
    }
    public String setprevious_weeks_volume(){
        this.name = previous_weeks_volume;
    }
    public String getnext_weeks_open(){
        return next_weeks_open;
    }
    public String setnext_weeks_open(){
        this.name = next_weeks_open;
    }
    public String getnext_weeks_close(){
        return next_weeks_close;
    }
    public String setnext_weeks_close(){
        this.name = next_weeks_close;
    }
    public String getpercent_change_next_weeks_price(){
        return percent_change_next_weeks_price;
    }
    public String setpercent_change_next_weeks_price(){
        this.name = percent_change_next_weeks_price;
    }
    public String getdays_to_next_dividend(){
        return days_to_next_dividend;
    }
    public String setdays_to_next_dividend(){
        this.name = days_to_next_dividend;
    }
    public String getpercent_return_next_dividend(){
        return percent_return_next_dividend;
    }
    public String setpercent_return_next_dividend(){
        this.name = percent_return_next_dividend;
    }

    public SimpleDateFormat formatDate(String date){ 
        String pattern = "yyyy-MM-dd";
        SimpleDateFormat simpleDateFormat = new SimpleDateFormat(pattern, date);
        //example output
        //String date = simpleDateFormat.format(new Date());
        return simpleDateFormat;
    }

    public static void main(String[] args) throws AnalysisException {
        // $example on:init_session$
        SparkSession spark = SparkSession
        .builder()
        .appName("Java Spark SQL Query MySQL Database & Write Java DataFrames")
        .config("spark.some.config.option", "config")
        .getOrCreate();

        runQuerySaveJavaDF(spark);

        spark.stop();
    }

    private static void runQuerySaveJavaDF(SparkSession spark) {

        SQLContext sqlContext = new org.apache.spark.sql.SQLContext(spark);
        //https://spark.apache.org/docs/1.5.2/sql-programming-guide.html#interoperating-with-rdds

        String jdbcHostname = "104.154.56.191";
        Int jdbcPort = 3306;
        String jdbcDatabase = "djuci";
        
        // Create the JDBC URL without passing in the user and password parameters.
        String jdbcUrl = "jdbc:mysql://${jdbcHostname}:${jdbcPort}/${jdbcDatabase}";

        // Note: JDBC loading and saving can be achieved via either the load/save or jdbc methods
        // Loading data from a JDBC source
        Dataset<Row> jdbcDF = spark.read()
        .format("jdbc")
        .option("url", "jdbc:mysql://${jdbcHostname}:${jdbcPort}/${jdbcDatabase}")
        .option("data", "schema.tablename")
        .option("user", "root")
        .option("password", "Srping2019!!")
        .load();

        jdbcDF.printSchema();
        jdbcDF.show();

    }
}