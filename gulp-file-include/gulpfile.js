var gulp =require('gulp');//引入gulp

var fileinclude  =require('gulp-file-include');//引入gulp-file-include

gulp.task('fileinclude', function(done) {

    gulp.src('src/**.html') .pipe(fileinclude({//gulp.src中存放要编译的文件

           prefix:'@@',

           basepath:'@file'

    })).pipe(gulp.dest('dist'));//gulp.dest中存放编译后的文件的存放地址
    done();

});
