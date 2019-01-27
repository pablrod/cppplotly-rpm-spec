Name: cppplotly
Version: 0.2.0
Release: 1%{?dist}
Summary: Generate html/javascript charts from C++ data using javascript library plotly.js

License: MIT 
URL: https://github.com/pablrod/cppplotly
Source0: %{url}/archive/v%{version}.tar.gz

BuildRequires: cmake >= 3.1.0
BuildRequires: gcc-c++ >= 5.3.1      
BuildRequires: json11 >= 1.0.0      
Requires: json11 >= 1.0.0      

%define debug_package %{nil}

%description
Library to generate html/javascript charts directly in C++ using javascript library plotly.js

%package devel
Summary: Development files for CppPlotly

%description devel
Header files for development using C++ library CppPlotly. This library is header only

%prep
%autosetup


%build
cmake -DCMAKE_INSTALL_PREFIX=/usr .
%make_build


%install
rm -rf $RPM_BUILD_ROOT
%make_install


%files devel
%license LICENSE
%doc README.md
%{_includedir}/CppPlotly/BaseTrace.h
%{_includedir}/CppPlotly/Plot.h
%{_includedir}/CppPlotly/Trace/Box/Line.h
%{_includedir}/CppPlotly/Trace/Box/Hoverlabel/Font.h
%{_includedir}/CppPlotly/Trace/Box/Stream.h
%{_includedir}/CppPlotly/Trace/Box/Unselected.h
%{_includedir}/CppPlotly/Trace/Box/Unselected/Marker.h
%{_includedir}/CppPlotly/Trace/Box/Selected/Marker.h
%{_includedir}/CppPlotly/Trace/Box/Selected.h
%{_includedir}/CppPlotly/Trace/Box/Hoverlabel.h
%{_includedir}/CppPlotly/Trace/Box/Marker.h
%{_includedir}/CppPlotly/Trace/Box/Marker/Line.h
%{_includedir}/CppPlotly/Trace/Box/Transform.h
%{_includedir}/CppPlotly/Trace/Scattermapbox/Line.h
%{_includedir}/CppPlotly/Trace/Scattermapbox/Hoverlabel/Font.h
%{_includedir}/CppPlotly/Trace/Scattermapbox/Textfont.h
%{_includedir}/CppPlotly/Trace/Scattermapbox/Stream.h
%{_includedir}/CppPlotly/Trace/Scattermapbox/Unselected.h
%{_includedir}/CppPlotly/Trace/Scattermapbox/Unselected/Marker.h
%{_includedir}/CppPlotly/Trace/Scattermapbox/Selected/Marker.h
%{_includedir}/CppPlotly/Trace/Scattermapbox/Selected.h
%{_includedir}/CppPlotly/Trace/Scattermapbox/Hoverlabel.h
%{_includedir}/CppPlotly/Trace/Scattermapbox/Marker.h
%{_includedir}/CppPlotly/Trace/Scattermapbox/Marker/Colorbar.h
%{_includedir}/CppPlotly/Trace/Scattermapbox/Marker/Colorbar/Tickformatstop.h
%{_includedir}/CppPlotly/Trace/Scattermapbox/Marker/Colorbar/Titlefont.h
%{_includedir}/CppPlotly/Trace/Scattermapbox/Marker/Colorbar/Tickfont.h
%{_includedir}/CppPlotly/Trace/Scattermapbox/Transform.h
%{_includedir}/CppPlotly/Trace/Scattergeo.h
%{_includedir}/CppPlotly/Trace/Choropleth.h
%{_includedir}/CppPlotly/Trace/Scattergl/Line.h
%{_includedir}/CppPlotly/Trace/Scattergl/Hoverlabel/Font.h
%{_includedir}/CppPlotly/Trace/Scattergl/Stream.h
%{_includedir}/CppPlotly/Trace/Scattergl/Error_x.h
%{_includedir}/CppPlotly/Trace/Scattergl/Unselected.h
%{_includedir}/CppPlotly/Trace/Scattergl/Unselected/Marker.h
%{_includedir}/CppPlotly/Trace/Scattergl/Error_y.h
%{_includedir}/CppPlotly/Trace/Scattergl/Selected/Marker.h
%{_includedir}/CppPlotly/Trace/Scattergl/Selected.h
%{_includedir}/CppPlotly/Trace/Scattergl/Hoverlabel.h
%{_includedir}/CppPlotly/Trace/Scattergl/Marker.h
%{_includedir}/CppPlotly/Trace/Scattergl/Marker/Line.h
%{_includedir}/CppPlotly/Trace/Scattergl/Marker/Colorbar.h
%{_includedir}/CppPlotly/Trace/Scattergl/Marker/Colorbar/Tickformatstop.h
%{_includedir}/CppPlotly/Trace/Scattergl/Marker/Colorbar/Titlefont.h
%{_includedir}/CppPlotly/Trace/Scattergl/Marker/Colorbar/Tickfont.h
%{_includedir}/CppPlotly/Trace/Scattergl/Transform.h
%{_includedir}/CppPlotly/Trace/Parcoords.h
%{_includedir}/CppPlotly/Trace/Candlestick/Line.h
%{_includedir}/CppPlotly/Trace/Candlestick/Hoverlabel/Font.h
%{_includedir}/CppPlotly/Trace/Candlestick/Increasing/Line.h
%{_includedir}/CppPlotly/Trace/Candlestick/Stream.h
%{_includedir}/CppPlotly/Trace/Candlestick/Increasing.h
%{_includedir}/CppPlotly/Trace/Candlestick/Decreasing/Line.h
%{_includedir}/CppPlotly/Trace/Candlestick/Decreasing.h
%{_includedir}/CppPlotly/Trace/Candlestick/Hoverlabel.h
%{_includedir}/CppPlotly/Trace/Candlestick/Transform.h
%{_includedir}/CppPlotly/Trace/Cone.h
%{_includedir}/CppPlotly/Trace/Sankey.h
%{_includedir}/CppPlotly/Trace/Parcoords/Line.h
%{_includedir}/CppPlotly/Trace/Parcoords/Hoverlabel/Font.h
%{_includedir}/CppPlotly/Trace/Parcoords/Domain.h
%{_includedir}/CppPlotly/Trace/Parcoords/Stream.h
%{_includedir}/CppPlotly/Trace/Parcoords/Dimension.h
%{_includedir}/CppPlotly/Trace/Parcoords/Tickfont.h
%{_includedir}/CppPlotly/Trace/Parcoords/Line/Colorbar.h
%{_includedir}/CppPlotly/Trace/Parcoords/Line/Colorbar/Tickformatstop.h
%{_includedir}/CppPlotly/Trace/Parcoords/Line/Colorbar/Titlefont.h
%{_includedir}/CppPlotly/Trace/Parcoords/Line/Colorbar/Tickfont.h
%{_includedir}/CppPlotly/Trace/Parcoords/Hoverlabel.h
%{_includedir}/CppPlotly/Trace/Parcoords/Transform.h
%{_includedir}/CppPlotly/Trace/Parcoords/Rangefont.h
%{_includedir}/CppPlotly/Trace/Parcoords/Labelfont.h
%{_includedir}/CppPlotly/Trace/Scatter.h
%{_includedir}/CppPlotly/Trace/Pie/Hoverlabel/Font.h
%{_includedir}/CppPlotly/Trace/Pie/Domain.h
%{_includedir}/CppPlotly/Trace/Pie/Textfont.h
%{_includedir}/CppPlotly/Trace/Pie/Stream.h
%{_includedir}/CppPlotly/Trace/Pie/Hoverlabel.h
%{_includedir}/CppPlotly/Trace/Pie/Marker.h
%{_includedir}/CppPlotly/Trace/Pie/Insidetextfont.h
%{_includedir}/CppPlotly/Trace/Pie/Marker/Line.h
%{_includedir}/CppPlotly/Trace/Pie/Outsidetextfont.h
%{_includedir}/CppPlotly/Trace/Pie/Transform.h
%{_includedir}/CppPlotly/Trace/Mesh3d.h
%{_includedir}/CppPlotly/Trace/Scatter3d/Line.h
%{_includedir}/CppPlotly/Trace/Scatter3d/Hoverlabel/Font.h
%{_includedir}/CppPlotly/Trace/Scatter3d/Textfont.h
%{_includedir}/CppPlotly/Trace/Scatter3d/Stream.h
%{_includedir}/CppPlotly/Trace/Scatter3d/Error_x.h
%{_includedir}/CppPlotly/Trace/Scatter3d/Error_y.h
%{_includedir}/CppPlotly/Trace/Scatter3d/Error_z.h
%{_includedir}/CppPlotly/Trace/Scatter3d/Projection/Y.h
%{_includedir}/CppPlotly/Trace/Scatter3d/Projection/Z.h
%{_includedir}/CppPlotly/Trace/Scatter3d/Projection/X.h
%{_includedir}/CppPlotly/Trace/Scatter3d/Hoverlabel.h
%{_includedir}/CppPlotly/Trace/Scatter3d/Marker.h
%{_includedir}/CppPlotly/Trace/Scatter3d/Marker/Line.h
%{_includedir}/CppPlotly/Trace/Scatter3d/Marker/Colorbar.h
%{_includedir}/CppPlotly/Trace/Scatter3d/Marker/Colorbar/Tickformatstop.h
%{_includedir}/CppPlotly/Trace/Scatter3d/Marker/Colorbar/Titlefont.h
%{_includedir}/CppPlotly/Trace/Scatter3d/Marker/Colorbar/Tickfont.h
%{_includedir}/CppPlotly/Trace/Scatter3d/Transform.h
%{_includedir}/CppPlotly/Trace/Scatter3d/Projection.h
%{_includedir}/CppPlotly/Trace/Carpet.h
%{_includedir}/CppPlotly/Trace/Heatmapgl.h
%{_includedir}/CppPlotly/Trace/Bar/Hoverlabel/Font.h
%{_includedir}/CppPlotly/Trace/Bar/Textfont.h
%{_includedir}/CppPlotly/Trace/Bar/Stream.h
%{_includedir}/CppPlotly/Trace/Bar/Error_x.h
%{_includedir}/CppPlotly/Trace/Bar/Unselected.h
%{_includedir}/CppPlotly/Trace/Bar/Unselected/Textfont.h
%{_includedir}/CppPlotly/Trace/Bar/Unselected/Marker.h
%{_includedir}/CppPlotly/Trace/Bar/Error_y.h
%{_includedir}/CppPlotly/Trace/Bar/Selected/Textfont.h
%{_includedir}/CppPlotly/Trace/Bar/Selected/Marker.h
%{_includedir}/CppPlotly/Trace/Bar/Selected.h
%{_includedir}/CppPlotly/Trace/Bar/Hoverlabel.h
%{_includedir}/CppPlotly/Trace/Bar/Marker.h
%{_includedir}/CppPlotly/Trace/Bar/Insidetextfont.h
%{_includedir}/CppPlotly/Trace/Bar/Marker/Line.h
%{_includedir}/CppPlotly/Trace/Bar/Marker/Colorbar.h
%{_includedir}/CppPlotly/Trace/Bar/Marker/Colorbar/Tickformatstop.h
%{_includedir}/CppPlotly/Trace/Bar/Marker/Colorbar/Titlefont.h
%{_includedir}/CppPlotly/Trace/Bar/Marker/Colorbar/Tickfont.h
%{_includedir}/CppPlotly/Trace/Bar/Outsidetextfont.h
%{_includedir}/CppPlotly/Trace/Bar/Transform.h
%{_includedir}/CppPlotly/Trace/Pointcloud.h
%{_includedir}/CppPlotly/Trace/Scatterternary.h
%{_includedir}/CppPlotly/Trace/Histogram/Hoverlabel/Font.h
%{_includedir}/CppPlotly/Trace/Histogram/Ybins.h
%{_includedir}/CppPlotly/Trace/Histogram/Xbins/ImpliedEdits.h
%{_includedir}/CppPlotly/Trace/Histogram/Xbins.h
%{_includedir}/CppPlotly/Trace/Histogram/Stream.h
%{_includedir}/CppPlotly/Trace/Histogram/Error_x.h
%{_includedir}/CppPlotly/Trace/Histogram/Unselected.h
%{_includedir}/CppPlotly/Trace/Histogram/Unselected/Textfont.h
%{_includedir}/CppPlotly/Trace/Histogram/Unselected/Marker.h
%{_includedir}/CppPlotly/Trace/Histogram/Error_y.h
%{_includedir}/CppPlotly/Trace/Histogram/Selected/Textfont.h
%{_includedir}/CppPlotly/Trace/Histogram/Selected/Marker.h
%{_includedir}/CppPlotly/Trace/Histogram/Selected.h
%{_includedir}/CppPlotly/Trace/Histogram/Cumulative.h
%{_includedir}/CppPlotly/Trace/Histogram/Hoverlabel.h
%{_includedir}/CppPlotly/Trace/Histogram/Marker.h
%{_includedir}/CppPlotly/Trace/Histogram/Ybins/ImpliedEdits.h
%{_includedir}/CppPlotly/Trace/Histogram/Marker/Line.h
%{_includedir}/CppPlotly/Trace/Histogram/Marker/Colorbar.h
%{_includedir}/CppPlotly/Trace/Histogram/Marker/Colorbar/Tickformatstop.h
%{_includedir}/CppPlotly/Trace/Histogram/Marker/Colorbar/Titlefont.h
%{_includedir}/CppPlotly/Trace/Histogram/Marker/Colorbar/Tickfont.h
%{_includedir}/CppPlotly/Trace/Histogram/Transform.h
%{_includedir}/CppPlotly/Trace/Choropleth/Hoverlabel/Font.h
%{_includedir}/CppPlotly/Trace/Choropleth/Colorbar.h
%{_includedir}/CppPlotly/Trace/Choropleth/Stream.h
%{_includedir}/CppPlotly/Trace/Choropleth/Unselected.h
%{_includedir}/CppPlotly/Trace/Choropleth/Colorbar/Tickformatstop.h
%{_includedir}/CppPlotly/Trace/Choropleth/Colorbar/Titlefont.h
%{_includedir}/CppPlotly/Trace/Choropleth/Colorbar/Tickfont.h
%{_includedir}/CppPlotly/Trace/Choropleth/Unselected/Marker.h
%{_includedir}/CppPlotly/Trace/Choropleth/Selected/Marker.h
%{_includedir}/CppPlotly/Trace/Choropleth/Selected.h
%{_includedir}/CppPlotly/Trace/Choropleth/Hoverlabel.h
%{_includedir}/CppPlotly/Trace/Choropleth/Marker.h
%{_includedir}/CppPlotly/Trace/Choropleth/Marker/Line.h
%{_includedir}/CppPlotly/Trace/Choropleth/Transform.h
%{_includedir}/CppPlotly/Trace/Scatter3d.h
%{_includedir}/CppPlotly/Trace/Area/Hoverlabel/Font.h
%{_includedir}/CppPlotly/Trace/Area/Stream.h
%{_includedir}/CppPlotly/Trace/Area/Hoverlabel.h
%{_includedir}/CppPlotly/Trace/Area/Marker.h
%{_includedir}/CppPlotly/Trace/Area/Transform.h
%{_includedir}/CppPlotly/Trace/Heatmapgl/Hoverlabel/Font.h
%{_includedir}/CppPlotly/Trace/Heatmapgl/Colorbar.h
%{_includedir}/CppPlotly/Trace/Heatmapgl/Stream.h
%{_includedir}/CppPlotly/Trace/Heatmapgl/Colorbar/Tickformatstop.h
%{_includedir}/CppPlotly/Trace/Heatmapgl/Colorbar/Titlefont.h
%{_includedir}/CppPlotly/Trace/Heatmapgl/Colorbar/Tickfont.h
%{_includedir}/CppPlotly/Trace/Heatmapgl/Hoverlabel.h
%{_includedir}/CppPlotly/Trace/Heatmapgl/Transform.h
%{_includedir}/CppPlotly/Trace/Table.h
%{_includedir}/CppPlotly/Trace/Scattergl.h
%{_includedir}/CppPlotly/Trace/Scatterternary/Line.h
%{_includedir}/CppPlotly/Trace/Scatterternary/Hoverlabel/Font.h
%{_includedir}/CppPlotly/Trace/Scatterternary/Textfont.h
%{_includedir}/CppPlotly/Trace/Scatterternary/Stream.h
%{_includedir}/CppPlotly/Trace/Scatterternary/Unselected.h
%{_includedir}/CppPlotly/Trace/Scatterternary/Unselected/Textfont.h
%{_includedir}/CppPlotly/Trace/Scatterternary/Unselected/Marker.h
%{_includedir}/CppPlotly/Trace/Scatterternary/Selected/Textfont.h
%{_includedir}/CppPlotly/Trace/Scatterternary/Selected/Marker.h
%{_includedir}/CppPlotly/Trace/Scatterternary/Selected.h
%{_includedir}/CppPlotly/Trace/Scatterternary/Hoverlabel.h
%{_includedir}/CppPlotly/Trace/Scatterternary/Marker.h
%{_includedir}/CppPlotly/Trace/Scatterternary/Marker/Line.h
%{_includedir}/CppPlotly/Trace/Scatterternary/Marker/Colorbar.h
%{_includedir}/CppPlotly/Trace/Scatterternary/Marker/Gradient.h
%{_includedir}/CppPlotly/Trace/Scatterternary/Marker/Colorbar/Tickformatstop.h
%{_includedir}/CppPlotly/Trace/Scatterternary/Marker/Colorbar/Titlefont.h
%{_includedir}/CppPlotly/Trace/Scatterternary/Marker/Colorbar/Tickfont.h
%{_includedir}/CppPlotly/Trace/Scatterternary/Transform.h
%{_includedir}/CppPlotly/Trace/Scattergeo/Line.h
%{_includedir}/CppPlotly/Trace/Scattergeo/Hoverlabel/Font.h
%{_includedir}/CppPlotly/Trace/Scattergeo/Textfont.h
%{_includedir}/CppPlotly/Trace/Scattergeo/Stream.h
%{_includedir}/CppPlotly/Trace/Scattergeo/Unselected.h
%{_includedir}/CppPlotly/Trace/Scattergeo/Unselected/Textfont.h
%{_includedir}/CppPlotly/Trace/Scattergeo/Unselected/Marker.h
%{_includedir}/CppPlotly/Trace/Scattergeo/Selected/Textfont.h
%{_includedir}/CppPlotly/Trace/Scattergeo/Selected/Marker.h
%{_includedir}/CppPlotly/Trace/Scattergeo/Selected.h
%{_includedir}/CppPlotly/Trace/Scattergeo/Hoverlabel.h
%{_includedir}/CppPlotly/Trace/Scattergeo/Marker.h
%{_includedir}/CppPlotly/Trace/Scattergeo/Marker/Line.h
%{_includedir}/CppPlotly/Trace/Scattergeo/Marker/Colorbar.h
%{_includedir}/CppPlotly/Trace/Scattergeo/Marker/Gradient.h
%{_includedir}/CppPlotly/Trace/Scattergeo/Marker/Colorbar/Tickformatstop.h
%{_includedir}/CppPlotly/Trace/Scattergeo/Marker/Colorbar/Titlefont.h
%{_includedir}/CppPlotly/Trace/Scattergeo/Marker/Colorbar/Tickfont.h
%{_includedir}/CppPlotly/Trace/Scattergeo/Transform.h
%{_includedir}/CppPlotly/Trace/Splom/Hoverlabel/Font.h
%{_includedir}/CppPlotly/Trace/Splom/Stream.h
%{_includedir}/CppPlotly/Trace/Splom/Unselected.h
%{_includedir}/CppPlotly/Trace/Splom/Dimension.h
%{_includedir}/CppPlotly/Trace/Splom/Unselected/Marker.h
%{_includedir}/CppPlotly/Trace/Splom/Selected/Marker.h
%{_includedir}/CppPlotly/Trace/Splom/Diagonal.h
%{_includedir}/CppPlotly/Trace/Splom/Selected.h
%{_includedir}/CppPlotly/Trace/Splom/Hoverlabel.h
%{_includedir}/CppPlotly/Trace/Splom/Marker.h
%{_includedir}/CppPlotly/Trace/Splom/Marker/Line.h
%{_includedir}/CppPlotly/Trace/Splom/Marker/Colorbar.h
%{_includedir}/CppPlotly/Trace/Splom/Marker/Colorbar/Tickformatstop.h
%{_includedir}/CppPlotly/Trace/Splom/Marker/Colorbar/Titlefont.h
%{_includedir}/CppPlotly/Trace/Splom/Marker/Colorbar/Tickfont.h
%{_includedir}/CppPlotly/Trace/Splom/Transform.h
%{_includedir}/CppPlotly/Trace/Contourcarpet.h
%{_includedir}/CppPlotly/Trace/Scatterpolar/Line.h
%{_includedir}/CppPlotly/Trace/Scatterpolar/Hoverlabel/Font.h
%{_includedir}/CppPlotly/Trace/Scatterpolar/Textfont.h
%{_includedir}/CppPlotly/Trace/Scatterpolar/Stream.h
%{_includedir}/CppPlotly/Trace/Scatterpolar/Unselected.h
%{_includedir}/CppPlotly/Trace/Scatterpolar/Unselected/Textfont.h
%{_includedir}/CppPlotly/Trace/Scatterpolar/Unselected/Marker.h
%{_includedir}/CppPlotly/Trace/Scatterpolar/Selected/Textfont.h
%{_includedir}/CppPlotly/Trace/Scatterpolar/Selected/Marker.h
%{_includedir}/CppPlotly/Trace/Scatterpolar/Selected.h
%{_includedir}/CppPlotly/Trace/Scatterpolar/Hoverlabel.h
%{_includedir}/CppPlotly/Trace/Scatterpolar/Marker.h
%{_includedir}/CppPlotly/Trace/Scatterpolar/Marker/Line.h
%{_includedir}/CppPlotly/Trace/Scatterpolar/Marker/Colorbar.h
%{_includedir}/CppPlotly/Trace/Scatterpolar/Marker/Gradient.h
%{_includedir}/CppPlotly/Trace/Scatterpolar/Marker/Colorbar/Tickformatstop.h
%{_includedir}/CppPlotly/Trace/Scatterpolar/Marker/Colorbar/Titlefont.h
%{_includedir}/CppPlotly/Trace/Scatterpolar/Marker/Colorbar/Tickfont.h
%{_includedir}/CppPlotly/Trace/Scatterpolar/Transform.h
%{_includedir}/CppPlotly/Trace/Surface.h
%{_includedir}/CppPlotly/Trace/Cone/Hoverlabel/Font.h
%{_includedir}/CppPlotly/Trace/Cone/Colorbar.h
%{_includedir}/CppPlotly/Trace/Cone/Lightposition.h
%{_includedir}/CppPlotly/Trace/Cone/Stream.h
%{_includedir}/CppPlotly/Trace/Cone/Colorbar/Tickformatstop.h
%{_includedir}/CppPlotly/Trace/Cone/Colorbar/Titlefont.h
%{_includedir}/CppPlotly/Trace/Cone/Colorbar/Tickfont.h
%{_includedir}/CppPlotly/Trace/Cone/Hoverlabel.h
%{_includedir}/CppPlotly/Trace/Cone/Lighting.h
%{_includedir}/CppPlotly/Trace/Cone/Transform.h
%{_includedir}/CppPlotly/Trace/Scattercarpet/Line.h
%{_includedir}/CppPlotly/Trace/Scattercarpet/Hoverlabel/Font.h
%{_includedir}/CppPlotly/Trace/Scattercarpet/Textfont.h
%{_includedir}/CppPlotly/Trace/Scattercarpet/Stream.h
%{_includedir}/CppPlotly/Trace/Scattercarpet/Unselected.h
%{_includedir}/CppPlotly/Trace/Scattercarpet/Unselected/Textfont.h
%{_includedir}/CppPlotly/Trace/Scattercarpet/Unselected/Marker.h
%{_includedir}/CppPlotly/Trace/Scattercarpet/Selected/Textfont.h
%{_includedir}/CppPlotly/Trace/Scattercarpet/Selected/Marker.h
%{_includedir}/CppPlotly/Trace/Scattercarpet/Selected.h
%{_includedir}/CppPlotly/Trace/Scattercarpet/Hoverlabel.h
%{_includedir}/CppPlotly/Trace/Scattercarpet/Marker.h
%{_includedir}/CppPlotly/Trace/Scattercarpet/Marker/Line.h
%{_includedir}/CppPlotly/Trace/Scattercarpet/Marker/Colorbar.h
%{_includedir}/CppPlotly/Trace/Scattercarpet/Marker/Gradient.h
%{_includedir}/CppPlotly/Trace/Scattercarpet/Marker/Colorbar/Tickformatstop.h
%{_includedir}/CppPlotly/Trace/Scattercarpet/Marker/Colorbar/Titlefont.h
%{_includedir}/CppPlotly/Trace/Scattercarpet/Marker/Colorbar/Tickfont.h
%{_includedir}/CppPlotly/Trace/Scattercarpet/Transform.h
%{_includedir}/CppPlotly/Trace/Contour/Line.h
%{_includedir}/CppPlotly/Trace/Contour/Hoverlabel/Font.h
%{_includedir}/CppPlotly/Trace/Contour/Colorbar.h
%{_includedir}/CppPlotly/Trace/Contour/Stream.h
%{_includedir}/CppPlotly/Trace/Contour/Colorbar/Tickformatstop.h
%{_includedir}/CppPlotly/Trace/Contour/Colorbar/Titlefont.h
%{_includedir}/CppPlotly/Trace/Contour/Colorbar/Tickfont.h
%{_includedir}/CppPlotly/Trace/Contour/Contours/ImpliedEdits.h
%{_includedir}/CppPlotly/Trace/Contour/Contours/Labelfont.h
%{_includedir}/CppPlotly/Trace/Contour/Hoverlabel.h
%{_includedir}/CppPlotly/Trace/Contour/Contours.h
%{_includedir}/CppPlotly/Trace/Contour/Transform.h
%{_includedir}/CppPlotly/Trace/Histogram2d/Hoverlabel/Font.h
%{_includedir}/CppPlotly/Trace/Histogram2d/Ybins.h
%{_includedir}/CppPlotly/Trace/Histogram2d/Colorbar.h
%{_includedir}/CppPlotly/Trace/Histogram2d/Xbins/ImpliedEdits.h
%{_includedir}/CppPlotly/Trace/Histogram2d/Xbins.h
%{_includedir}/CppPlotly/Trace/Histogram2d/Stream.h
%{_includedir}/CppPlotly/Trace/Histogram2d/Colorbar/Tickformatstop.h
%{_includedir}/CppPlotly/Trace/Histogram2d/Colorbar/Titlefont.h
%{_includedir}/CppPlotly/Trace/Histogram2d/Colorbar/Tickfont.h
%{_includedir}/CppPlotly/Trace/Histogram2d/Hoverlabel.h
%{_includedir}/CppPlotly/Trace/Histogram2d/Marker.h
%{_includedir}/CppPlotly/Trace/Histogram2d/Ybins/ImpliedEdits.h
%{_includedir}/CppPlotly/Trace/Histogram2d/Transform.h
%{_includedir}/CppPlotly/Trace/Scatterpolargl.h
%{_includedir}/CppPlotly/Trace/Histogram.h
%{_includedir}/CppPlotly/Trace/Ohlc.h
%{_includedir}/CppPlotly/Trace/Scattermapbox.h
%{_includedir}/CppPlotly/Trace/Pointcloud/Hoverlabel/Font.h
%{_includedir}/CppPlotly/Trace/Pointcloud/Stream.h
%{_includedir}/CppPlotly/Trace/Pointcloud/Hoverlabel.h
%{_includedir}/CppPlotly/Trace/Pointcloud/Marker.h
%{_includedir}/CppPlotly/Trace/Pointcloud/Marker/Border.h
%{_includedir}/CppPlotly/Trace/Pointcloud/Transform.h
%{_includedir}/CppPlotly/Trace/Contourcarpet/Line.h
%{_includedir}/CppPlotly/Trace/Contourcarpet/Hoverlabel/Font.h
%{_includedir}/CppPlotly/Trace/Contourcarpet/Colorbar.h
%{_includedir}/CppPlotly/Trace/Contourcarpet/Stream.h
%{_includedir}/CppPlotly/Trace/Contourcarpet/Colorbar/Tickformatstop.h
%{_includedir}/CppPlotly/Trace/Contourcarpet/Colorbar/Titlefont.h
%{_includedir}/CppPlotly/Trace/Contourcarpet/Colorbar/Tickfont.h
%{_includedir}/CppPlotly/Trace/Contourcarpet/Contours/ImpliedEdits.h
%{_includedir}/CppPlotly/Trace/Contourcarpet/Contours/Labelfont.h
%{_includedir}/CppPlotly/Trace/Contourcarpet/Hoverlabel.h
%{_includedir}/CppPlotly/Trace/Contourcarpet/Contours.h
%{_includedir}/CppPlotly/Trace/Contourcarpet/Transform.h
%{_includedir}/CppPlotly/Trace/Surface/Hoverlabel/Font.h
%{_includedir}/CppPlotly/Trace/Surface/Colorbar.h
%{_includedir}/CppPlotly/Trace/Surface/Lightposition.h
%{_includedir}/CppPlotly/Trace/Surface/Stream.h
%{_includedir}/CppPlotly/Trace/Surface/Colorbar/Tickformatstop.h
%{_includedir}/CppPlotly/Trace/Surface/Colorbar/Titlefont.h
%{_includedir}/CppPlotly/Trace/Surface/Colorbar/Tickfont.h
%{_includedir}/CppPlotly/Trace/Surface/Contours/Z/Project.h
%{_includedir}/CppPlotly/Trace/Surface/Contours/X/Project.h
%{_includedir}/CppPlotly/Trace/Surface/Contours/Y.h
%{_includedir}/CppPlotly/Trace/Surface/Contours/Y/Project.h
%{_includedir}/CppPlotly/Trace/Surface/Contours/Z.h
%{_includedir}/CppPlotly/Trace/Surface/Contours/X.h
%{_includedir}/CppPlotly/Trace/Surface/Hoverlabel.h
%{_includedir}/CppPlotly/Trace/Surface/Lighting.h
%{_includedir}/CppPlotly/Trace/Surface/Contours.h
%{_includedir}/CppPlotly/Trace/Surface/Transform.h
%{_includedir}/CppPlotly/Trace/Scattercarpet.h
%{_includedir}/CppPlotly/Trace/Ohlc/Line.h
%{_includedir}/CppPlotly/Trace/Ohlc/Hoverlabel/Font.h
%{_includedir}/CppPlotly/Trace/Ohlc/Increasing/Line.h
%{_includedir}/CppPlotly/Trace/Ohlc/Stream.h
%{_includedir}/CppPlotly/Trace/Ohlc/Increasing.h
%{_includedir}/CppPlotly/Trace/Ohlc/Decreasing/Line.h
%{_includedir}/CppPlotly/Trace/Ohlc/Decreasing.h
%{_includedir}/CppPlotly/Trace/Ohlc/Hoverlabel.h
%{_includedir}/CppPlotly/Trace/Ohlc/Transform.h
%{_includedir}/CppPlotly/Trace/Mesh3d/Hoverlabel/Font.h
%{_includedir}/CppPlotly/Trace/Mesh3d/Colorbar.h
%{_includedir}/CppPlotly/Trace/Mesh3d/Lightposition.h
%{_includedir}/CppPlotly/Trace/Mesh3d/Stream.h
%{_includedir}/CppPlotly/Trace/Mesh3d/Colorbar/Tickformatstop.h
%{_includedir}/CppPlotly/Trace/Mesh3d/Colorbar/Titlefont.h
%{_includedir}/CppPlotly/Trace/Mesh3d/Colorbar/Tickfont.h
%{_includedir}/CppPlotly/Trace/Mesh3d/Hoverlabel.h
%{_includedir}/CppPlotly/Trace/Mesh3d/Contour.h
%{_includedir}/CppPlotly/Trace/Mesh3d/Lighting.h
%{_includedir}/CppPlotly/Trace/Mesh3d/Transform.h
%{_includedir}/CppPlotly/Trace/Contour.h
%{_includedir}/CppPlotly/Trace/Carpet/Aaxis/Tickformatstop.h
%{_includedir}/CppPlotly/Trace/Carpet/Aaxis/Titlefont.h
%{_includedir}/CppPlotly/Trace/Carpet/Aaxis/Tickfont.h
%{_includedir}/CppPlotly/Trace/Carpet/Baxis.h
%{_includedir}/CppPlotly/Trace/Carpet/Hoverlabel/Font.h
%{_includedir}/CppPlotly/Trace/Carpet/Stream.h
%{_includedir}/CppPlotly/Trace/Carpet/Baxis/Tickformatstop.h
%{_includedir}/CppPlotly/Trace/Carpet/Baxis/Titlefont.h
%{_includedir}/CppPlotly/Trace/Carpet/Baxis/Tickfont.h
%{_includedir}/CppPlotly/Trace/Carpet/Aaxis.h
%{_includedir}/CppPlotly/Trace/Carpet/Hoverlabel.h
%{_includedir}/CppPlotly/Trace/Carpet/Font.h
%{_includedir}/CppPlotly/Trace/Carpet/Transform.h
%{_includedir}/CppPlotly/Trace/Sankey/Hoverlabel/Font.h
%{_includedir}/CppPlotly/Trace/Sankey/Domain.h
%{_includedir}/CppPlotly/Trace/Sankey/Textfont.h
%{_includedir}/CppPlotly/Trace/Sankey/Stream.h
%{_includedir}/CppPlotly/Trace/Sankey/Link/Line.h
%{_includedir}/CppPlotly/Trace/Sankey/Node.h
%{_includedir}/CppPlotly/Trace/Sankey/Link.h
%{_includedir}/CppPlotly/Trace/Sankey/Hoverlabel.h
%{_includedir}/CppPlotly/Trace/Sankey/Node/Line.h
%{_includedir}/CppPlotly/Trace/Sankey/Transform.h
%{_includedir}/CppPlotly/Trace/Table/Hoverlabel/Font.h
%{_includedir}/CppPlotly/Trace/Table/Domain.h
%{_includedir}/CppPlotly/Trace/Table/Cells.h
%{_includedir}/CppPlotly/Trace/Table/Stream.h
%{_includedir}/CppPlotly/Trace/Table/Cells/Line.h
%{_includedir}/CppPlotly/Trace/Table/Cells/Fill.h
%{_includedir}/CppPlotly/Trace/Table/Cells/Font.h
%{_includedir}/CppPlotly/Trace/Table/Header/Line.h
%{_includedir}/CppPlotly/Trace/Table/Header/Fill.h
%{_includedir}/CppPlotly/Trace/Table/Header/Font.h
%{_includedir}/CppPlotly/Trace/Table/Header.h
%{_includedir}/CppPlotly/Trace/Table/Hoverlabel.h
%{_includedir}/CppPlotly/Trace/Table/Transform.h
%{_includedir}/CppPlotly/Trace/Candlestick.h
%{_includedir}/CppPlotly/Trace/Scatter/Line.h
%{_includedir}/CppPlotly/Trace/Scatter/Hoverlabel/Font.h
%{_includedir}/CppPlotly/Trace/Scatter/Textfont.h
%{_includedir}/CppPlotly/Trace/Scatter/Stream.h
%{_includedir}/CppPlotly/Trace/Scatter/Error_x.h
%{_includedir}/CppPlotly/Trace/Scatter/Unselected.h
%{_includedir}/CppPlotly/Trace/Scatter/Unselected/Textfont.h
%{_includedir}/CppPlotly/Trace/Scatter/Unselected/Marker.h
%{_includedir}/CppPlotly/Trace/Scatter/Error_y.h
%{_includedir}/CppPlotly/Trace/Scatter/Selected/Textfont.h
%{_includedir}/CppPlotly/Trace/Scatter/Selected/Marker.h
%{_includedir}/CppPlotly/Trace/Scatter/Selected.h
%{_includedir}/CppPlotly/Trace/Scatter/Hoverlabel.h
%{_includedir}/CppPlotly/Trace/Scatter/Marker.h
%{_includedir}/CppPlotly/Trace/Scatter/Marker/Line.h
%{_includedir}/CppPlotly/Trace/Scatter/Marker/Colorbar.h
%{_includedir}/CppPlotly/Trace/Scatter/Marker/Gradient.h
%{_includedir}/CppPlotly/Trace/Scatter/Marker/Colorbar/Tickformatstop.h
%{_includedir}/CppPlotly/Trace/Scatter/Marker/Colorbar/Titlefont.h
%{_includedir}/CppPlotly/Trace/Scatter/Marker/Colorbar/Tickfont.h
%{_includedir}/CppPlotly/Trace/Scatter/Transform.h
%{_includedir}/CppPlotly/Trace/Scatterpolar.h
%{_includedir}/CppPlotly/Trace/Heatmap.h
%{_includedir}/CppPlotly/Trace/Histogram2dcontour.h
%{_includedir}/CppPlotly/Trace/Heatmap/Hoverlabel/Font.h
%{_includedir}/CppPlotly/Trace/Heatmap/Colorbar.h
%{_includedir}/CppPlotly/Trace/Heatmap/Stream.h
%{_includedir}/CppPlotly/Trace/Heatmap/Colorbar/Tickformatstop.h
%{_includedir}/CppPlotly/Trace/Heatmap/Colorbar/Titlefont.h
%{_includedir}/CppPlotly/Trace/Heatmap/Colorbar/Tickfont.h
%{_includedir}/CppPlotly/Trace/Heatmap/Hoverlabel.h
%{_includedir}/CppPlotly/Trace/Heatmap/Transform.h
%{_includedir}/CppPlotly/Trace/Histogram2dcontour/Line.h
%{_includedir}/CppPlotly/Trace/Histogram2dcontour/Hoverlabel/Font.h
%{_includedir}/CppPlotly/Trace/Histogram2dcontour/Ybins.h
%{_includedir}/CppPlotly/Trace/Histogram2dcontour/Colorbar.h
%{_includedir}/CppPlotly/Trace/Histogram2dcontour/Xbins/ImpliedEdits.h
%{_includedir}/CppPlotly/Trace/Histogram2dcontour/Xbins.h
%{_includedir}/CppPlotly/Trace/Histogram2dcontour/Stream.h
%{_includedir}/CppPlotly/Trace/Histogram2dcontour/Colorbar/Tickformatstop.h
%{_includedir}/CppPlotly/Trace/Histogram2dcontour/Colorbar/Titlefont.h
%{_includedir}/CppPlotly/Trace/Histogram2dcontour/Colorbar/Tickfont.h
%{_includedir}/CppPlotly/Trace/Histogram2dcontour/Contours/ImpliedEdits.h
%{_includedir}/CppPlotly/Trace/Histogram2dcontour/Contours/Labelfont.h
%{_includedir}/CppPlotly/Trace/Histogram2dcontour/Hoverlabel.h
%{_includedir}/CppPlotly/Trace/Histogram2dcontour/Marker.h
%{_includedir}/CppPlotly/Trace/Histogram2dcontour/Ybins/ImpliedEdits.h
%{_includedir}/CppPlotly/Trace/Histogram2dcontour/Contours.h
%{_includedir}/CppPlotly/Trace/Histogram2dcontour/Transform.h
%{_includedir}/CppPlotly/Trace/Violin/Line.h
%{_includedir}/CppPlotly/Trace/Violin/Box/Line.h
%{_includedir}/CppPlotly/Trace/Violin/Hoverlabel/Font.h
%{_includedir}/CppPlotly/Trace/Violin/Stream.h
%{_includedir}/CppPlotly/Trace/Violin/Unselected.h
%{_includedir}/CppPlotly/Trace/Violin/Unselected/Marker.h
%{_includedir}/CppPlotly/Trace/Violin/Selected/Marker.h
%{_includedir}/CppPlotly/Trace/Violin/Selected.h
%{_includedir}/CppPlotly/Trace/Violin/Hoverlabel.h
%{_includedir}/CppPlotly/Trace/Violin/Marker.h
%{_includedir}/CppPlotly/Trace/Violin/Meanline.h
%{_includedir}/CppPlotly/Trace/Violin/Marker/Line.h
%{_includedir}/CppPlotly/Trace/Violin/Box.h
%{_includedir}/CppPlotly/Trace/Violin/Transform.h
%{_includedir}/CppPlotly/Trace/Area.h
%{_includedir}/CppPlotly/Trace/Box.h
%{_includedir}/CppPlotly/Trace/Pie.h
%{_includedir}/CppPlotly/Trace/Histogram2d.h
%{_includedir}/CppPlotly/Trace/Bar.h
%{_includedir}/CppPlotly/Trace/Splom.h
%{_includedir}/CppPlotly/Trace/Scatterpolargl/Line.h
%{_includedir}/CppPlotly/Trace/Scatterpolargl/Hoverlabel/Font.h
%{_includedir}/CppPlotly/Trace/Scatterpolargl/Stream.h
%{_includedir}/CppPlotly/Trace/Scatterpolargl/Unselected.h
%{_includedir}/CppPlotly/Trace/Scatterpolargl/Unselected/Textfont.h
%{_includedir}/CppPlotly/Trace/Scatterpolargl/Unselected/Marker.h
%{_includedir}/CppPlotly/Trace/Scatterpolargl/Selected/Textfont.h
%{_includedir}/CppPlotly/Trace/Scatterpolargl/Selected/Marker.h
%{_includedir}/CppPlotly/Trace/Scatterpolargl/Selected.h
%{_includedir}/CppPlotly/Trace/Scatterpolargl/Hoverlabel.h
%{_includedir}/CppPlotly/Trace/Scatterpolargl/Marker.h
%{_includedir}/CppPlotly/Trace/Scatterpolargl/Marker/Line.h
%{_includedir}/CppPlotly/Trace/Scatterpolargl/Marker/Colorbar.h
%{_includedir}/CppPlotly/Trace/Scatterpolargl/Marker/Colorbar/Tickformatstop.h
%{_includedir}/CppPlotly/Trace/Scatterpolargl/Marker/Colorbar/Titlefont.h
%{_includedir}/CppPlotly/Trace/Scatterpolargl/Marker/Colorbar/Tickfont.h
%{_includedir}/CppPlotly/Trace/Scatterpolargl/Transform.h
%{_includedir}/CppPlotly/Trace/Violin.h

%changelog
* Sun Jan 27 2019 Pablo Rodríguez González <pablo.rodriguez.gonzalez@gmail.com>
- Created SPEC file for RPM from CppPlotly version 0.2.0
